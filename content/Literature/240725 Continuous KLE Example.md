---
title: Continuous KLE Example
draft: false
tags:
---
In the following we assume that $a$ is a random process, i.e., $a: \Theta \times\left[a_1, b_1\right] \rightarrow$ $\mathbb{R}$ with the Karhunen-Loève expansion
$$
a(\theta, r)=\mu_a(r)+\sum_{i=1}^{\infty} \sqrt{\lambda_i} \varphi_i(r) \xi_i(\theta)
$$
where $\lambda_i, \varphi_i$ refer to the eigenvalues and eigenfunctions that satisfy the equation $\int_{a_1}^{b_1} \operatorname{cov}_a\left(r, r^{\prime}\right) \varphi_i(r) d r=\lambda_i \varphi_i\left(r^{\prime}\right)$, with $\operatorname{cov}_a$ being the covariance function of $a$. For the eigenfunctions, the orthogonality relation $\int_{a_1}^{b_1} \varphi_i(r) \varphi_j(r) \mathrm{d} r=\delta_{i j}$ holds.

1. Derive an expression for $\xi_i$ in the Karhunen-Loève expansion.

Hint: Multiply throughout by $\varphi_j(r)$, integrate with respect to $r$, and use the orthogonality relation.

![[../Files/Pasted image 20240827132223.png|center]]

2. Express the covariance function of $a$ in terms of eigenvalues and eigenfunctions of the Karhunen-Loève expansion. You can assume that the $\xi_i$ are mean-free and orthogonal with unit variance.

![[../Files/Pasted image 20240827132242.png|center]]

