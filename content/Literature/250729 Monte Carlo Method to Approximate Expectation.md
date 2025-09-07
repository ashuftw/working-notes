---
title: Monte Carlo Method to Approximate Expectation
draft: false
tags:
date: 2025-07-29
---
[[250729 Monte Carlo Methods|Monte Carlo]] approximation for an expected value is given as: 

$$
\boxed{
\mu\approx\tilde{\mu}_{K}:=\frac{1}{k}\sum_{i=1}^{K}y^{(i)}=\frac{1}{k}\sum_{i=1}^{K}\mathcal{M}(x^{(i)})}
$$
Where, 
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
