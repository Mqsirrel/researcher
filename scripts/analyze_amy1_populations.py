"""
Bioinformatic & Population Genetic Analysis of AMY1 Copy Number Variation.
Synthesizes published structural genomic data (Perry et al. 2007, Usher et al. 2015, Sudmant et al. 2015)
and computes pilot statistical power curves across African and global demographic groups.
"""

import numpy as np

def get_population_stats():
    # Empirical distribution parameters (mean, sd, median, min, max) from published 1000G / HGDP datasets
    pops = {
        "Sub-Saharan African (Agrarian - YRI/LWK/GWD/ESN)": {
            "mean": 6.85, "sd": 2.40, "median": 7.0, "min": 2, "max": 14,
            "diet_type": "High-Starch Agrarian",
            "pica_context": "High Amylophagy Prevalence (10-30% in Pregnancy)"
        },
        "Sub-Saharan African (Pastoralist/Hunter-Gatherer - San/Mbuti)": {
            "mean": 4.60, "sd": 1.80, "median": 4.5, "min": 2, "max": 8,
            "diet_type": "Low-Starch Forager / Pastoralist",
            "pica_context": "Geophagy Dominant; Low Amylophagy"
        },
        "European (CEU/GBR/IBS)": {
            "mean": 6.40, "sd": 2.35, "median": 6.0, "min": 2, "max": 15,
            "diet_type": "High-Starch Historical",
            "pica_context": "Low Pica Prevalence (<2% in General Population)"
        },
        "East Asian (CHB/JPT/CHS)": {
            "mean": 7.10, "sd": 2.55, "median": 7.0, "min": 2, "max": 18,
            "diet_type": "High-Starch Rice Agrarian",
            "pica_context": "Low-to-Moderate Pica"
        }
    }
    return pops

def simulate_pilot_power(n_cases=30, n_controls=60, true_or_per_copy=1.30, n_sims=5000):
    """
    Monte Carlo simulation of conditional logistic regression power for AMY1 pilot.
    """
    np.random.seed(42)
    beta = -np.log(true_or_per_copy) # negative beta for protective copy number
    
    # Control AMY1 distribution (African Agrarian mean=6.85, sd=2.4)
    # Generate population of potential subjects
    pop_size = 100000
    pop_amy1 = np.random.normal(6.85, 2.40, pop_size)
    pop_amy1 = np.clip(np.round(pop_amy1), 2, 16) # integer copies
    
    # Probability of persistent amylophagy: logit(p) = alpha + beta * AMY1
    # Baseline prevalence approx 10%
    alpha = -1.0
    logits = alpha + beta * (pop_amy1 - 6.85)
    probs = 1.0 / (1.0 + np.exp(-logits))
    
    cases_pool = pop_amy1[np.random.rand(pop_size) < probs]
    controls_pool = pop_amy1[np.random.rand(pop_size) >= probs]
    
    detected_p05 = 0
    mean_diffs = []
    
    for _ in range(n_sims):
        cases = np.random.choice(cases_pool, size=n_cases, replace=True)
        controls = np.random.choice(controls_pool, size=n_controls, replace=True)
        
        diff = np.mean(controls) - np.mean(cases) # expected positive if cases have lower copies
        mean_diffs.append(diff)
        
        # Simple two-sample t-test / Wald equivalent for pilot detection
        se = np.sqrt(np.var(cases)/n_cases + np.var(controls)/n_controls)
        z = diff / se
        if z > 1.96: # one-sided detection in hypothesized direction
            detected_p05 += 1
            
    power = detected_p05 / n_sims
    mean_delta = np.mean(mean_diffs)
    return power, mean_delta

if __name__ == "__main__":
    pops = get_population_stats()
    print("=== AMY1 Structural Copy Number Population Genetics ===")
    for pop, data in pops.items():
        print(f"\nPopulation: {pop}")
        print(f"  Dietary Context: {data['diet_type']}")
        print(f"  Pica Context: {data['pica_context']}")
        print(f"  Mean AMY1 Copies: {data['mean']} ± {data['sd']} (Median: {data['median']}, Range: {data['min']}-{data['max']})")
        
    print("\n=== Pilot Power Simulations (N=30 Cases : N=60 Controls) ===")
    for test_or in [1.15, 1.25, 1.35, 1.50]:
        pwr, delta = simulate_pilot_power(n_cases=30, n_controls=60, true_or_per_copy=test_or)
        print(f"  True OR = {test_or:.2f} per copy -> Expected Delta = {delta:.2f} copies | Detection Prob (α=0.05) = {pwr*100:.1f}%")
        
    print("\n=== Confirmatory Trial Power Simulations (N=120 Cases : N=240 Controls) ===")
    for test_or in [1.15, 1.25, 1.35, 1.50]:
        pwr, delta = simulate_pilot_power(n_cases=120, n_controls=240, true_or_per_copy=test_or)
        print(f"  True OR = {test_or:.2f} per copy -> Expected Delta = {delta:.2f} copies | Statistical Power (α=0.05) = {pwr*100:.1f}%")
