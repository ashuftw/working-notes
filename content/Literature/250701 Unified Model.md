---
title: Unified Model
draft: false
tags: 
date: 2025-07-01
---
The unified model is a mathematical framework showing that many regression algorithms can be expressed in a single, general form.

## Mathematical Formulation


$$
t(x) = \sum_{e=1}^{E} \phi_e(x, \theta_e)(w_e^T x + b_e)
$$


### Components
- $\phi_e(x, \theta_e)$: Basis functions (typically Gaussian/RBF)
- $w_e^T$: Weight vectors for local linear models
- $b_e$: Bias/offset terms
- $E$: Number of local models
- $\theta_e$: Parameters of basis functions (e.g., mean, variance)
## Deconstructing the Model
For any given $x$ , the model calculates which expert is most relevant and gives its output more weight in the final sum.


$$
t(x)=\sum_{e=1}^E \text{Weight for Expert} (e) \times  \text{Prediction from Expert} (e)
$$


**Prediction from Expert**
This is the simple linear model ( $w_e^T x+b_e$ ). Each of the $E$ "experts" is a linear model with its own weight vector $w_e$ and bias $b_e$.

**Weight for Expert**
This is the gating function $\phi_e\left(x, \theta_e\right)$. It calculates a value based on the input $x$. Typically, these gating functions are designed to be high for some regions of the input space and low for others.

