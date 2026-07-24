---
title: Mean-Square Error of the Monte-Carlo Method
draft: false
tags:
date: 2025-09-04
---
Mathematically, there holds:
$$
\mathbb{E}\left[\left|\mu-\hat{\mu}_K\right|^2\right]=\mathbb{V}\left[\hat{\mu}_K\right]+\overbrace{\left(\mu-\mathbb{E}\left[\hat{\mu}_K\right]\right)^2}^0
$$
where,
- $\mu$ -> True but unknown Expected value
- $\mu-\mathbb{E}\left[\hat{\mu}_K\right]$ -> is called the bias.

1. ***The Monte Carlo method is unbiased, i.e.,***


	$$
	\mathbb{E}\left[\hat{\mu}_K\right]=\mu
	$$


2. If $\mathbb{V}[Y]<\infty$, the mean-square error (MSE) satisfies


	$$
	\mathbb{E}\left[\left|\mu-\hat{\mu}_K\right|^2\right]=\mathbb{V}\left[\hat{\mu}_K\right]=\frac{\mathbb{V}[Y]}{K} .
	$$


	Where,
	- $\mathbb{V}[Y]$ -> is the Variance of the model's output random variable $Y$
	- The MSE is independent of the number of uncertain input parameters.
	- There are different ways to reduce the error:
	- Increase sample size $K$ (can be very expensive if the model is complex)
	- Decrease variance (Quasi-Monte Carlo, control variate method, multilevel Monte Carlo)
	