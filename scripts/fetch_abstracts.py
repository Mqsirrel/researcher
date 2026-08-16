#!/usr/bin/env python3
"""Helper script to search and fetch abstracts from PubMed via NCBI E-utilities."""
import urllib.request
import urllib.parse
import json
import xml.etree.ElementTree as ET
import sys

def search_pubmed(query: str, max_results: int = 15):
    url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term={urllib.parse.quote(query)}&retmode=json&retmax={max_results}"
    req = urllib.request.Request(url, headers={"User-Agent": "AutonomousBiomedicalResearcher/1.0"})
    with urllib.request.urlopen(req) as resp:
        data = json.loads(resp.read().decode("utf-8"))
    return data.get("esearchresult", {}).get("idlist", [])

def fetch_details(pmids: list[str]):
    if not pmids:
        return []
    pmid_str = ",".join(pmids)
    url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id={pmid_str}&retmode=xml"
    req = urllib.request.Request(url, headers={"User-Agent": "AutonomousBiomedicalResearcher/1.0"})
    with urllib.request.urlopen(req) as resp:
        xml_data = resp.read()
    
    root = ET.fromstring(xml_data)
    articles = []
    for article in root.findall(".//PubmedArticle"):
        pmid = article.findtext(".//MedlineCitation/PMID")
        title = article.findtext(".//ArticleTitle") or "No title"
        abstract_elems = article.findall(".//Abstract/AbstractText")
        abstract = " ".join([elem.text for elem in abstract_elems if elem.text]) if abstract_elems else "No abstract"
        journal = article.findtext(".//Journal/Title") or "Unknown journal"
        year = article.findtext(".//JournalIssue/PubDate/Year") or article.findtext(".//JournalIssue/PubDate/MedlineDate") or "Unknown year"
        articles.append({
            "pmid": pmid,
            "title": title,
            "journal": journal,
            "year": year,
            "abstract": abstract
        })
    return articles

if __name__ == "__main__":
    if len(sys.argv) > 1:
        query = " ".join(sys.argv[1:])
        print(f"Searching for: {query}")
        ids = search_pubmed(query)
        print(f"Found IDs: {ids}")
        results = fetch_details(ids)
        for r in results:
            print(f"\n--- PMID: {r['pmid']} ({r['year']}) ---")
            print(f"Title: {r['title']}")
            print(f"Journal: {r['journal']}")
            print(f"Abstract: {r['abstract'][:500]}...")
