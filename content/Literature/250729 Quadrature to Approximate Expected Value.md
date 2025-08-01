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

**Note:**
- Polynomials of degree $2 n_{q u}-1$ or less are integrated exactly.
- Points $\left(x^{(i)}\right)_{i=1}^{n_{q u}}$ are chosen as roots of polynomials $\Phi_i$ satisfying:
$$
\int_{\Xi_\chi} \Phi_i(x) \Phi_j(x) f_\chi(x) \mathrm{d} x \propto \delta_{i j}
$$
 