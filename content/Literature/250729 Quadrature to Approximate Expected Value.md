---
title: Quadrature to Approximate Expected Value
draft: false
tags: 
date: 2025-07-29
---
The general formula is an approximation based on a weighted sum of the model evaluated at specific points:
$$
\mathbb{E}[\mathcal{M}(X)]=\int_{\Xi_X} \mathcal{M}(x) f_X(x) \mathrm{d} x \approx \sum_{i=1}^{n_{\text {qu }}} w^{(i)} \mathcal{M}\left(x^{(i)}\right)
$$
* $x^{(i)}$ -> the integration points or nodes
* $w^{(i)}$ -> the integration weights
- $\int_{\mathbb{\Xi}_{x}}$ -> represents integral over the [[250729 Support of a Distribution|support]]
- $\mathcal M$ -> model function

## Key Principle 

The key principle is to achieve the highest possible accuracy for integrating polynomials. A Gauss rule with $n_{qu}$ points can **exactly integrate polynomials of degree $2n_{qu} - 1$ or less**.

The nodes are chosen as the roots of polynomials that are **orthogonal** with respect to the input variable's PDF ($f_X(x)$) as the weighting function.
**Note:**

- Points $\left(x^{(i)}\right)_{i=1}^{n_{q u}}$ are chosen as roots of polynomials $\Phi_i$ satisfying:


	$$
	\int_{\Xi_\chi} \Phi_i(x) \Phi_j(x) f_\chi(x) \mathrm{d} x \propto \delta_{i j}
	$$


 