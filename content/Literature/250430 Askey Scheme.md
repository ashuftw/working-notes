---
title: Askey Scheme
draft: false
tags: 
date: 2025-04-30
---

## Use case:

It is used to [[250429 Orthogonality|Orthogonal]] Basis functions for the [[230731 General Polynomial Chaos Expansion (GPC)|Polynomial Chaos Expansion]]

| Distribution | Basis function    |
| ------------ | ----------------- |
| Normal       | Hermit Polynomial |
| Uniform      | Legendre          |
| Gamma        | Laguerre          |
| Beta         | Jacobi            |

### Example

| Hermit Polynomial   | Value                     |
| ------------------- | ------------------------- |
| $H_0(\xi)$          | 1                         |
| $H_1(\xi)$          | $\xi$                     |
| $H_2(\xi)$          | $\xi^2 - 1$               |
| ...                 | ...                       |

| LEGENDRE POLYNOMIAL | VALUE                     |
| ------------------- | ------------------------- |
| $P_0(\xi)$          | $1$                       |
| $P_1(\xi)$          | $\xi$                     |
| $P_2(\xi)$          | $\frac{1}{2}(3\xi^2 - 1)$ |
| ...                 | ...                       |
