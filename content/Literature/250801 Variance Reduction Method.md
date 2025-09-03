---
title: Variance Reduction Method
draft: false
tags:
date: 2025-09-01
---
**Variance reduction** techniques aim to decrease the [[250901 Mean-Square Error of the Monte-Carlo Method|mean-square error]] of a [[250729 Monte Carlo Methods|Monte Carlo]] estimate without necessarily increasing the number of samples. For an estimate of the mean value, the error is given by:
$$
\mathbb{E}\left[\left|\mu-\hat{\mu}_K\right|^2\right]=\mathbb{V}\left[\hat{\mu}_K\right]=\frac{\mathbb{V}[Y]}{K} .
$$
Reducing the variance $\mathbb{V}[Y]$ directly [[250901 Reducing Errors in Monte Carlo Methods|improves the accuracy]] of the simulation.
### Examples of variance reduction methods
- [[250801 Control Variate Method|Control Variate Method]]
- [[250901 Multilevel Monte Carlo (MLMC)|Multilevel Monte Carlo (MLMC)]]