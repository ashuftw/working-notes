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


## Relating Models to the Unified Model

### 1. **Simple Linear Regression**

- **Setting**: $E = 1$, $\phi_1(x) = 1$ (constant everywhere)
- **Result**: $t(x) = w^T x + b$
- **Interpretation**: One global linear model, no local weighting

### 2. **RBF (Radial Basis Function) Networks**

- **Setting**: $w_e = 0$ (zero weight vectors), keep only $b_e$
- **Result**: $t(x) = \sum_{j=1}^{J} \phi_j(x, \theta_j) \cdot b_j$
- **Interpretation**: Weighted sum of constants, each Gaussian holds one value

### 3. **Weighted Regression (WR)**

- **Setting**: $E = 1$, but $\phi(x)$ varies with input
- **Result**: $t(x) = \phi(x)(w^T x + b)$
- **Interpretation**: Single linear model weighted by input-dependent function

### 4. **Locally Weighted Regression (LWR)**

- **Setting**: Full unified model with all parameters
- **Result**: $t(x) = \sum_{e=1}^{E} \phi_e(x, \theta_e)(w_e^T x + b_e)$
- **Interpretation**: Multiple local linear models, each weighted by Gaussian

### Key Relationships:

- **RBF ⊂ LWR**: RBF is special case of LWR with $w_e = 0$
- **Linear Regression ⊂ LWR**: Linear regression is LWR with $E=1$, $\phi=1$
- **LWR = Most General**: Can represent all others by parameter choices
#### Hierarchy of complexity
**Linear Regression → RBF → LWR** 