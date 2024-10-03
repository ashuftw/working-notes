---
title: non-Intrusive Surrogate Modeling
draft: false
date: 2024-07-23
---

### From Orthogonal Projection the following analogies are drawn

| Linear algebra              | Probability                                         |
| --------------------------- | --------------------------------------------------- |
| Dot product                 | Expectation                                         |
| $\textbf a$                 | Model $Y = \mathcal{M}(\boldsymbol{\zeta})$         |
| $\textbf c^\textbf a$       | Surrogate $\tilde{\mathcal{M}}(\boldsymbol{\zeta})$ |
| plane $\mathcal P$          | **gPC** space                                       |
| basis vectors $\textbf b_i$ | **gPC** basis $\Phi_i$                              |

![[Pasted image 20240723121603.png|center|700]]
#### **∴** gPC Coefficient is given by

$$
q_i=\frac{\mathbb{E}\left[\mathcal{M}(\xi) \Phi_i(\xi)\right]}{\mathbb{E}\left[\Phi_i(\xi)^2\right]}
$$

#### Projected gPC expansion 

$$
\mathcal Y \approx \widetilde{\mathcal{M}}(\xi)=\sum_{i=0}^n \frac{\mathbb{E}\left[\mathcal{M}(\xi) \Phi_i(\xi)\right]}{\mathbb{E}\left[\Phi_i(\xi)^2\right]} \Phi_i(\xi)
$$




 where  $\textbf c^\textbf a$ is the projected point given by $\left[c^a=\frac{\left(a \cdot b_1\right)}{b_1 \cdot b_1} b_1+\frac{\left(a \cdot b_2\right)}{b_2 \cdot b_2} b_2\right]$

