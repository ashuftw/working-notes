---
title: Generalized Linear Model
draft: false
tags: 
date: 2025-07-14
---
## Condition 
The [[250711 Bayesian Approach  to Classification|Bayesian Approach]] decomposes to the Generalized Linear Model when the [[240305 Normal or Gaussian Distribution|Gaussians]] that are modeling the class-conditional distributions, $p\left(x \mid C_k\right)$ share the same **covariance matrix** ($\Sigma$).

The formula for the posterior probability $p\left(C_1 \mid x\right)$ simplifies to the form of a [[250714 Sigmoid Function|sigmoid]] function applied to a linear equation:

$$
p\left(C_1 \mid x\right)=\sigma\left(w^T x+w_0\right)
$$


This structure is the definition of a generalized linear model (specifically, logistic regression). It has two key components:
1. **Linear Component:** The term inside the function, $w^T x+w_0$, is a linear combination of the input features $\mathbf{x}$.
2. **Non-linear "Link" Function:** The sigmoid function, $\sigma(\cdot)$, takes the output of the linear component and transforms it into a probability between $0$ and $1$.

Therefore, the Bayesian approach is not always a generalized linear model, but it effectively becomes one when you make the specific assumption of Gaussian classes with equal covariance, as the resulting model for the posterior probability perfectly fits the GLM structure.
