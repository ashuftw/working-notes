---
title: MAP = Regularized Least Squares
draft: false
tags: 
date: 2025-06-04
---
## MAP solution
A MAP estimation with a Gaussian prior on the weights and a Gaussian likelihood on the data is equivalent to minimizing the sum of squared errors with L2 regularization.
 $$
\text{MAP with Gaussian prior} = \text{Minimizing squared error + regularization}
$$

**Formula:**
$$
w_{M A P}=  \arg\max_w P(w|D) =  \arg \min _w\left[\underbrace{\frac{1}{2} \sum_n\left(t_n-w^T \phi\left(x_n\right)\right)^2}_{\text {from Likelihood (Squared Error) }}+\underbrace{\frac{\lambda}{2}\|w\|^2}_{\text {from Prior (L2 Regularization) }}\right]
$$

### Key Insight:
The regularization strength $\lambda$ is inversely proportional to the variance of the Gaussian prior $\left(\sigma_p^2\right)$ :
$$
\lambda=\frac{1}{\sigma_p^2}
$$
- Strong Regularization (large $\lambda$ ) $\leftrightarrow$ Small Prior Variance (weights are assumed to be near zero).
- Weak Regularization (small $\lambda$ ) $\leftrightarrow$ Large Prior Variance (weights are allowed to vary more).


**Key Point:** The model is **linear in parameters** $\mathbf{w}$ but can be **non-linear in inputs** $x$ through the choice of basis functions $\phi(x)$.