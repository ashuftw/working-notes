---
title: Discriminant Function for Minimum Error Rate Classification
draft: false
tags: 
date: 2025-08-14
---
For a minimum-error-rate classifier, several equivalent discriminant functions can be used, as the final decision only depends on which one is the maximum. Starting with the posterior probability:
1.  **Ideal form (Posterior Probability):**
    $$g_i(x) = P(s=i|x) = \frac{p(x|s=i)P(s=i)}{\sum_{j \in S}p(x|s=j)P(s=j)}$$
2.  **Simplified form (Ignoring the evidence):** Since the denominator (evidence) is the same for all classes, it can be dropped.
    $$g_i(x) = p(x|s=i)P(s=i)$$
3.  **Logarithmic form:** Taking the natural logarithm simplifies multiplication into addition, which is often computationally more stable and convenient.
    $$g_i(x) = \ln p(x|s=i) + \ln P(s=i)$$

	All these forms will yield the same classification result because they preserve the order of the discriminant values.

## Discriminant  function for a two-category, minimum-error-rate case.
$$
g(\mathbf{x})=g_1(\mathbf{x})-g_2(\mathbf{x})
$$

Decide for $s^*=1$, if $g(\mathbf{x})>0$
Decide for $s^*=2$, if $g(\mathbf{x})<0$
### Choice of Discriminant:
1.  **Based on Posterior Probabilities:** This is a direct comparison of the posterior probabilities for each class.
    $$g(x) = P(s=1|x) - P(s=2|x)$$

2.  **Based on Log-Likelihood Ratio (LLR):** This formulation is often more convenient as it separates the likelihoods from the priors and uses logarithms to convert products into sums.
    $$g(x) = \log\frac{P(x|s=1)}{P(x|s=2)} + \log\frac{P(s=1)}{P(s=2)}$$
    This is equivalent to the log-likelihood ratio plus the log of the prior odds.