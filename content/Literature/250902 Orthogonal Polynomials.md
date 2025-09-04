---
title: Orthogonal Polynomials
draft: true
tags:
date: 2025-09-02
---
In the context of **UQ**, **Orthogonal polynomials** are sets of polynomials $\{\Phi_i\}$ that are mutually orthogonal with respect to a specific weighting function, which is typically a probability density function (PDF).

Mathematically, a set of polynomials $\Phi_i(\xi)$ is orthogonal with respect to the PDF $f_{\xi}(t)$ of a random variable $\xi$ if their expected product is zero for different polynomials. This is expressed as:

$$
\mathbb{E}_{\xi}[\Phi_{i}(\xi)\Phi_{j}(\xi)] = \int_{\mathbb{R}}\Phi_{i}(t)\Phi_{j}(t)f_{\xi}(t)dt = c_{i}\delta_{ij}
$$

where:
- $\mathbb{E}_{\xi}[\cdot]$ is the expectation taken with respect to the random variable $\xi$.
- $\delta_{ij}$ is the Kronecker delta, which is 1 if $i=j$ and 0 otherwise.
- $c_i$ is a normalization constant. If $c_i=1$, the polynomials are called **orthonormal**.

**[[250902 Orthogonal Polynomials in gPC Expansions|Application]]**