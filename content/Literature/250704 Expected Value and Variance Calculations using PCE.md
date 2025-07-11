---
title: Expected Value and Variance Calculations using PCE
draft: false
tags: 
date: 2025-07-04
---
## Expected Value

$$
\boxed{
\mathbb{E}_{\xi}[X]=q_0
}
$$

**Derivation**

$$
\mathbb{E}_{\xi}[X]=\mathbb{E}_{\xi}\left[\sum_{i=0}^{\infty} q_i \Phi_i(\xi)\right]=\sum_{i=0}^{\infty} q_i \mathbb{E}_{\xi}\left[\Phi_i(\xi)\right]
$$


Since $\Phi_0=1$ and all higher-order polynomials are constructed to have zero mean (i.e., $\mathbb{E}\left[\Phi_i(\xi)\right]=0$ for $i>0$ ), we get:

$$
\mathbb{E}_{\xi}[X]=q_0 \cdot 1+\sum_{i=1}^{\infty} q_i \cdot 0=q_0
$$




## Variance

$$
\boxed{
\mathbb{V}_{\xi}[X]=\sum_{i=1}^{\infty} q_i^2}
$$


**Derivation**

$$
\mathbb{V}_{\xi}[X]=\mathbb{E}_{\xi}\left[\left(X-\mathbb{E}_{\xi}[X]\right)^2\right]=\mathbb{E}_{\xi}\left[\left(\sum_{i=0}^{\infty} q_i \Phi_i(\xi)-q_0\right)^2\right]
$$


Simplifying:

$$
\mathbb{V}_{\xi}[X]=\mathbb{E}_{\xi}\left[\left(\sum_{i=1}^{\infty} q_i \Phi_i(\xi)\right)^2\right]=\mathbb{E}_{\xi}\left[\sum_{i=1}^{\infty} \sum_{j=1}^{\infty} q_i q_j \Phi_i(\xi) \Phi_j(\xi)\right]
$$


Using orthonormality:

$$
\mathbb{V}_{\xi}[X]=\sum_{i=1}^{\infty} \sum_{j=1}^{\infty} q_i q_j \mathbb{E}_{\xi}\left[\Phi_i(\xi) \Phi_j(\xi)\right]=\sum_{i=1}^{\infty} \sum_{j=1}^{\infty} q_i q_j \delta_{i j}=\sum_{i=1}^{\infty} q_i^2
$$


Assuming $\xi$ is orthonormal.
