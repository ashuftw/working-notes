---
title: Monte Carlo Method to Approximate Expectation
draft: false
tags: 
date: 2025-07-29
---
[[250729 Monte Carlo Methods|Monte Carlo]] approximation for an expected value is given as: 

$$\boxed{
\mu\approx\tilde{\mu}_{K}:=\frac{1}{k}\sum_{i=1}^{K}y^{(i)}=\frac{1}{k}\sum_{i=1}^{K}\mathcal{M}(x^{(i)})}
$$
- $K$-> Total number of samples generated
- $x$ ->Random sample input which are independent and identically distributed (i.i.d.) realizations of the input random variable $X$.
- $\mathcal{M}(x^{(i)})$ Model, $\mathcal{M}$, when evaluated at the $i-$th random input sample, $x^{(i)}$
> Note: $y=\mathcal M(x)$ 

## Multi-dimensional Case
$$\boxed{
\mu=\mathbb{E}[\gamma] \approx \tilde{\mu}_K=\frac{1}{K} \sum_{i=1}^K y^{(i)}=\frac{1}{K} \sum_{i=1}^K \mathcal{M}\left(\mathbf{x}^{(i)}\right)}
$$
The sample $\left\{\mathbf{x}^{(i)}\right\}_{i=1}^K$ now contains vectors.
1. If $X_1, \ldots, X_{n_{\text {in }}}$ are **independent**:
	Generate $x_1^{(i)}, x_2^{(i)}, \ldots, x_{n_{\text {in }}}^{(i)}$ independently of each other
2. If $X_1, \ldots, X_{n_{\text {in }}}$ are **dependent**:
	Draw $\boldsymbol{x}{ }^{(i)}$ directly from the joint PDF $f_X$

## Calculation Steps
1.  Generate a sample of model inputs $\{x^{(i)}\}_{i=1}^{K}$.
2.  Compute the corresponding model output sample $\{y^{(i)}=\mathcal{M}(x^{(i)})\}_{i=1}^{K}$.
3.  Estimate the expected value using the mean of the output sample.

## Mean-Square Error of the Monte-Carlo Method
There holds:
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

2. If $\mathbb{V}[\gamma]<\infty$, the mean-square error (MSE) satisfies
	$$
	\mathbb{E}\left[\left|\mu-\hat{\mu}_K\right|^2\right]=\mathbb{V}\left[\hat{\mu}_K\right]=\frac{\mathbb{V}[\gamma]}{K} .
	$$
	Where,
	- $\mathbb{V}[\gamma]$ -> is the Variance of the model's output random variable $Y$
	- The MSE is independent of the number of uncertain input parameters.
	- There are different ways to reduce the error:
	- Increase sample size $K$ (can be very expensive if the model is complex)
	- Decrease variance (Quasi-Monte Carlo, control variate method, multilevel Monte Carlo)
	