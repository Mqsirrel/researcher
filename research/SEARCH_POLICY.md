# Token-Efficient Research Policy

The objective is **information gained per unit of search/model cost**, not maximum paper count.

## Before every search

Ask:

1. What uncertainty am I trying to reduce?
2. Which competing hypotheses would this search distinguish?
3. Has this question already been answered in `state/search-cache.md`?
4. What is the smallest search that could answer the question?
5. What result would change the hypothesis ranking?

If the answer to #3 is yes and no meaningful new dimension exists, do not repeat the search.

## Search ladder

Escalate only as needed:

1. Existing state/cache
2. Targeted keyword search
3. Synonym/terminology search
4. Citation follow-up
5. Adjacent-field search
6. Broad systematic search
7. Full-text/deep extraction

Do not jump to level 6–7 when level 1–3 can resolve the uncertainty.

## Stop searching when

- new papers are mostly redundant,
- the hypothesis ranking is stable,
- additional papers no longer change the mechanistic model,
- or the remaining uncertainty requires an experiment rather than more literature.

## Novelty exception

A promising N3/N4 hypothesis receives a temporary exception: perform a deliberate novelty sweep across synonyms, citation networks, adjacent fields and older terminology before accepting the novelty claim.

Even then, cache the novelty search so it is not repeated without a reason.

## Paper triage

Do not deeply read every result.

Classify first:

- likely irrelevant → discard
- relevant background → metadata/abstract only
- mechanistically relevant → extract evidence
- hypothesis-changing → full-text analysis
- potentially novelty-relevant → full-text + citation traversal

## Iteration rule

Every completed search must produce one of:

- hypothesis ranking changed,
- uncertainty reduced,
- contradiction discovered,
- new mechanistic edge discovered,
- search deemed redundant,
- or explicit reason why more evidence is needed.

If none occurred, the search strategy should be reconsidered before repeating it.
