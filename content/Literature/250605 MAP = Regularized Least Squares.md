---
title: 
draft: false
tags: 
date: 2025-06-04
---
This property arises from the fact:
- Gaussian likelihood $\rightarrow$ Squared error
- Gaussian prior $\rightarrow \mathrm{L} 2$ regularization

## MAP solution

**The math:**

$$
w_\text{MAP} = \arg\max_w P(w|D)= \arg\min_w \left[\underbrace{\frac{1}{2}\sum_n (t_n - w^T\phi(x_n))^2}_\text{from Likelihood} +\underbrace{\frac{\lambda}{2}||w||^2}_\text{Prior}\right]
$$

Therefore:
- MAP with Gaussian prior = Minimizing squared error + regularization
- Prior acts as regularizer
- $\lambda$ controls regularization strength $=$ prior variance

> **Key insight**: Probabilistic and deterministic approaches give the same answer!

Remember:
- Prior $\rightarrow$ Regularization
- No prior $\rightarrow$ No regularization (ML = unregularized least squares)
