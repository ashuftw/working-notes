---
title: Control Variate Method
draft: true
tags:
date: 2025-09-01
---
It is a **[[250801 Variance Reduction Method|variance reduction]]** technique used to improve the efficiency of Monte Carlo simulations when computing a mean value $\mathbb{E}[\mathcal{M}(X)]$.
### Core Idea
It uses a simpler, correlated model $\tilde{\mathcal{M}}(X)$, called the **control variate**, for which the exact mean value $\mathbb{E}[\tilde{\mathcal{M}}(X)]$ is known.

Instead of directly estimating $\mathbb{E}[\mathcal{M}(X)]$ we use the identity:
$$\mathbb{E}[\mathcal{M}(X)] = \mathbb{E}[\mathcal{M}(X) - \tilde{\mathcal{M}}(X)] + \mathbb{E}[\tilde{\mathcal{M}}(X)]$$
A Monte Carlo simulation is then performed on the difference term, $\mathcal{M}(X) - \tilde{\mathcal{M}}(X)$.

> Note: $\tilde{\mathcal{M}}(X)$ is can be a [[240305 Surrogate Modeling|surrogate model]] (Eg. [[230731 General Polynomial Chaos Expansion (GPC)|gPC]]) 
### Why It's Effective
If the control variate $\tilde{\mathcal{M}}$ is a good approximation of $\mathcal{M}$
$$
\mathbb{V}[\mathcal{M}(X) - \tilde{\mathcal{M}}(X)]\ll\mathbb{V}[\mathcal{M}(X)]
$$
This leads to a more accurate estimate for the same number of samples.
### Estimator
A generalized form of the estimator is:
$$\tilde{\mu}_{K}^{CV} := \frac{1}{K}\sum_{i=1}^{K}(\mathcal{M}(x^{(i)}) - \lambda\tilde{\mathcal{M}}(x^{(i)})) + \lambda\mathbb{E}[\tilde{\mathcal{M}}(X)]$$
Here, $\lambda$ is a coefficient chosen to minimize the variance of the estimator. The basic method simply uses $\lambda=1$.