---
title: Ordinary Least squares Solution
draft: false
tags: 
date: 2025-07-01
---


It is the **closed-form solution** for optimal parameters in a linear model, obtained by minimizing the [[250604 Squared Error Function|Squared Error Function]].


$$
\boxed{
w^* = (\Phi^T \Phi)^{-1} \Phi^T t
}
$$

## Components

- **$w^*$** = optimal weight/parameter vector
- **$\Phi$** = design matrix where $\Phi_{ij} = \phi_j(x_i)$
    - Each row = one data point
    - Each column = one basis function evaluated at all points
- **$t$** = target vector (all training outputs)

