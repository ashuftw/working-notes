---
title: Flashcards on Uncertainty Quantification
draft: true
tags: 
date: 2025-07-29
---
## Outlook
### How do Monte Carlo methods and Quadrature methods differ in their selection of points and weights?

* [[250729 Monte Carlo Method to Approximate Expectation]]: Uses random points ($x^{(i)}$) and uniform weights (e.g., $w^{(i)}=1/m$).
* [[250729 Quadrature to Approximate Expected Value|Quadrature]]: Uses deterministically chosen points and weights.

### How are the integration points for a Gauß quadrature rule chosen?
The points $(x^{(i)})$ are chosen as the roots of polynomials $\Phi_{j}$ that are orthogonal with respect to the weighting function $f_{x}(x)$. This is expressed by the relation: $$
\int_{\mathbb{\Xi}_{X}}\Phi_{i}(x)\Phi_{j}(x)f_{x}(x)dx\propto\delta_{ij}$$

### How can you approximate a general moment of order k, $\mathbb{M}^{k}[\mathcal{M}(X)]$, once you have a quadrature rule for the mean value?
The $k^{th}$ moment can be approximated by applying the same quadrature rule to the model output raised to the $k^{th}$ power.
$$
\mathbb{E}[\mathcal{M}(x)^{k}]\approx Q[\mathcal{M}(x)^{k}]=\sum_{i=1}^{n_{qu}}(\mathcal{M}(x^{(i)}))^{k}w^{(i)}
$$

### Under what conditions is the Monte Carlo method generally superior to n-dimensional quadrature rules?
The Monte Carlo method is superior whenever we have the condition 
$$
\frac s  n \le 0.5
$$ 
where, $s$ -> order of differentiability of the integrand and $n$ -> number of dimensions. 
This typically occurs in cases of:
* A large number of parameters (large $n$)
* Limited differentiability of the integrand (small $s$)
### What is the "curse-of-dimensionality" as it applies to tensor product quadrature?

The curse-of-dimensionality describes how the total number of quadrature points ($n_{qu}$) in a tensor rule grows exponentially with the number of input dimensions ($n$). The total number of points is the product of the points in each dimension: $n_{qu}=n_{qu;1}\cdot\cdot\cdot n_{qu;n}$.


### What are two methods to mitigate the curse-of-dimensionality in higher-dimensional quadrature?

1.  **Anisotropic rules**: These rules enhance efficiency by using a different number of nodes in each dimension, adapting to dimensions that are less important.
2.  **Sparse Grids**: These grids combine tensor grids of different orders to delay the curse-of-dimensionality.
### Is the standard Monte Carlo estimator biased or unbiased, and what does this mean for its Mean-Square Error (MSE)?
The standard Monte Carlo estimator is **unbiased**, meaning its expected value is the true value, $\mu$. This is a significant advantage because it simplifies the Mean-Square Error (MSE), making it equal to only the variance of the estimator, $\mathbb{V}[\hat{\mu}_{k}]$.

### What are the two fundamental strategies for accelerating Monte Carlo convergence?
1.  **Reduce the integrand's variance**: Transform the problem to effectively reduce the standard deviation $\sigma_{Y}$. An example is the Control Variate Method.
2.  **Modify the sampling strategy**: Generate the input points $\{x^{(i)}\}$ in a more structured way to achieve faster error reduction. An example is Quasi-Monte Carlo.

### In which two scenarios is the standard Monte Carlo method a particularly good choice?
The Monte Carlo method is especially useful when:
1.  The model involves many uncertain input parameters (high dimensionality).
2.  The model output is not smooth, exhibiting discontinuities or sharp variations.