---
title: Calculating Sobol Indices
draft: false
tags: 
date: 2025-07-04
---
### Example 1 
Given a random vector $\boldsymbol{X}=\left(X_1, X_2\right)$ and a model $\mathcal{M}(\boldsymbol{X})$, a PCE approximation has already been derived as

$$
\tilde{\mathcal{M}}(\boldsymbol{X}(\boldsymbol{\xi}))=\sum_{i=0}^3 q_i \Phi(\boldsymbol{X}(\boldsymbol{\xi})) .
$$


Consider the coefficients $q_i$ as given. The polynomials are also given as

$$
\begin{aligned}
& \Phi_0=1 \\
& \Phi_1=\xi_1 \\
& \Phi_2=\xi_2 \\
& \Phi_3=\xi_1 \xi_2
\end{aligned}
$$


Compute the first order and total Sobol indices.
#### Solution
**First Order [[250703 Sobol Indices|Sobol Indices]]** 

$$
S_i=\frac{D_i}{V[M(X)]}
$$

1. Total Variance [[250704 Expected Value and Variance Calculations using PCE|for PCE]]

$$
\mathbb{V}[\tilde M]=\sum_{i=1}^{3} q_i^2= q_1^2+ q_2^2+ q_3^2
$$

2. Solo-Effect Term: Only $\Phi_1=\xi_1$ corresponds to the solo effect of the first input.
3. Partial Variance Square of the the contributing coefficient =>$q_1^2$.

$$
S_1=\frac{D_1}{V[M(X)] }= \frac{q_1^2}{q_1^2+q_2^2+q_3^2}
$$


**Total Effect**

1. Polynomials involving $\xi_1$ -> $\Phi_1=\xi_1$ (the solo effect term) & $\Phi_3=\xi_1 \xi_2$ (the interaction term).
2. Partial Variance: $q_1^2+q_3^2$
3. Total Effect Index

$$
S_{T, 1}=\frac{q_1^2+q_3^2}{\sum_{i=1}^3 q_i^2}
$$

