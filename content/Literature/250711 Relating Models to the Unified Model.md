---
title: Relating Models to the Unified Model
draft: true
tags: 
date: 2025-07-11
---
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