---
title: Predictive vs Bayesian Predictive Distribution
draft: false
tags: 
date: 2025-06-05
---
![[../Files/Pasted image 20250704113926.png|center|650]]
## Mathematical Definition for a single prediction $t$
### 1. **Bayesian Predictive Distribution**
The Bayesian approach[^1](left plot) shows **wider uncertainty bands** because it accounts for parameter uncertainty on top of data noise. The uncertainty also **varies spatially** - being larger where there's less data.


$$
p(t|x, \mathbf{X}, \mathbf{T}) = \int p(t|x, w) p(w|\mathbf{X}, \mathbf{T}) dw = \mathcal{N}(t|m(x), s^2(x))
$$


- **Data-dependent mean:** $m(x)$
- **Input-dependent variance:** $s^2(x)$

**Note:** The weight $w$ is not explicitly included in the parameters on the LHS $(p(t∣x,\mathbf X,\mathbf T))$ of the Bayesian predictive distribution because it has been **integrated out**.
### 2. **Predictive Distribution** (Maximum Likelihood)
The Predictive Distribution uses a single "best" set of parameters found in the data. 


$$
p(t|x, w_{ML}, \beta_{ML}) = \mathcal{N}(t|y(x, w_{ML}), \beta_{ML}^{-1})
$$


- **Fixed mean:** $y(x, w_{ML})$
- **Fixed variance:** $\beta_{ML}^{-1}$ (constant for all inputs)

## Summary of key differences

**Predictive Distribution (Maximum Likelihood):**

- Uses **fixed parameters** $w_{ML}$ and $\beta_{ML}$ (point estimates)
- Uncertainty comes **only from data noise** (aleatoric uncertainty)
- Constant variance across all inputs

**Bayesian Predictive Distribution:**

- **Integrates over all possible parameters** weighted by their posterior probability
- Uncertainty comes from **both data noise AND parameter uncertainty** (aleatoric + epistemic)
- **Input-dependent variance** - uncertainty varies with location


[^1]: Help with the notation:
$p(t|x,X,T)$ is the **probability distribution of a new, unseen output $t$, conditioned on the new input $x$ and all the evidence from the training data, $X$ and $T$**.
