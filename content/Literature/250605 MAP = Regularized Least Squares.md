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
 $$
\text{MAP with Gaussian prior} = \text{Minimizing squared error + regularization}
$$
**Mathematically:**

$$
w_\text{MAP} = \arg\max_w P(w|D)= \arg\min_w \left[\underbrace{\frac{1}{2}\sum_n (t_n - \mathbf w^T\phi(x_n))^2}_\text{from Likelihood} +\underbrace{\frac{\lambda}{2}||\mathbf w||^2}_\text{Prior}\right]
$$

Therefore:
- Prior acts as regularizer
- $\lambda$ controls regularization strength $=$ prior variance

> **Key insight**: Probabilistic and deterministic approaches give the same answer!




**Key Point:** The model is **linear in parameters** $\mathbf{w}$ but can be **non-linear in inputs** $x$ through the choice of basis functions $\phi(x)$.