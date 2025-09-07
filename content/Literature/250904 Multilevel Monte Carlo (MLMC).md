---
title: Multilevel Monte Carlo Method (MLMC)
draft: false
tags:
date: 2025-09-04
---
The Multilevel Monte Carlo (MLMC) method is a **[[250801 Variance Reduction Method|variance reduction]]**  reduction technique that significantly accelerates Monte Carlo simulations by using a hierarchy of models with different levels of accuracy and computational cost.

## Use Case

It is ideal for models that can be solved at **multiple levels of discretization**, such as **finite element models** where the mesh resolution can be varied to alternate between accuracy and computational cost. 
## Core Idea 
It breaks down the problem using a ***"telescoping sum"*** identity such that
	$$
	\text{Final result = Estimate of Coarse Model + Series of Corrections from Finer levels }
	$$
- It runs a **large number of simulations** on the cheapest, coarsest model to get a baseline estimate.
- It runs a **small number of simulations** to estimate the *difference* (or correction) between successive levels.

## Why it's effective 

The method's power comes from the fact that the models at successive levels are **strongly correlated**.

-   **The variance of the difference** between two **adjacent levels** is much **smaller** than the variance of either **model** **individually**.
-   Because this variance is low, **very few samples** are needed to accurately estimate the correction terms.
-   This drastically reduces the number of required expensive, high-fidelity simulations, leading to a massive gain in computational efficiency for the same level of accuracy.
## Estimator

Similar to [[250901 Control Variate Method|Control Variate Method]] we split into estimating a cheap baseline and a low-variance correction.

$$
\mathbb{E}[\mathcal{M}_{1}(X)]=\mathbb{E}[\mathcal{M}_{0}(X)]+\mathbb{E}[\mathcal{M}_{1}(X)-\mathcal{M}_{0}(X)]
$$

Where:
-   **$\mathbb{E}[\mathcal{M}_{0}(X)]$**: The cheap, coarse baseline estimate.
-   **$\mathbb{E}[\mathcal{M}_{1}(X)]$**: The desired, expensive expected value.
-   **$\mathbb{E}[\mathcal{M}_{1}(X)-\mathcal{M}_{0}(X)]$**: The correction term, which has a very low variance and is cheap to estimate.

The MLMC estimator approximates the expected value of the finest level model, $\mathbb{E}[\mathcal{M}_L(X)]$, by summing the expected value of the coarsest model with a series of corrections from progressively finer model levels.

$$
\tilde{\mu}^{ML}_{K_0, ..., K_L} = \frac{1}{K_0} \sum_{j=1}^{K_0} \mathcal{M}_0(x^{(0,j)}) + \sum_{l=1}^{L} \frac{1}{K_l} \sum_{j=1}^{K_l} \left( \mathcal{M}_l(x^{(l,j)}) - \mathcal{M}_{l-1}(x^{(l,j)}) \right)
$$

Where:
-   **First Term**: Represents the standard Monte Carlo estimate using $K_0$ samples on the coarsest, cheapest model ($\mathcal{M}_0$).
-   **Second Term (Summation)**: Represents the sum of the estimated *corrections*. Each term in the sum estimates the difference between a finer level ($\mathcal{M}_l$) and the next-coarsest level ($\mathcal{M}_{l-1}$) using $K_l$ samples.