---
title: Monte Carlo Method to Approximate Variance
draft: false
tags:
date: 2025-09-02
---

The Monte Carlo estimate for the variance, $\mathbb{V}[Y]$, is given by the formula:

$$
\mathbb{V}[Y] \approx \frac{1}{K-1} \sum_{i=1}^{K} (\mathcal{M}(x^{(i)}) - \tilde{\mu}_{K})^2
$$


* **Generate Output Realizations**: A set of $K$ independent random input realizations, $\{x^{(i)}\}_{i=1}^{K}$, is generated. The model is then run for each of these inputs to get a corresponding set of output realizations, $\mathcal{M}(x^{(i)})$.

* **Estimate the Mean**: The mean of the output is estimated by averaging the output realizations from the previous step. This mean estimate is denoted as $\tilde{\mu}_{K}$.

* **Calculate Sum of Squared Differences**: For each output $\mathcal{M}(x^{(i)})$, the squared difference between it and the estimated mean $\tilde{\mu}_{K}$ is calculated. These squared differences are then summed up for all $K$ realizations.

* **Normalize the Sum**: The sum is multiplied by the factor $\frac{1}{K-1}$. The notes mention that this factor is used to create an "un-biased estimator," although using $\frac{1}{K}$ is also possible.