---
title: Regularisation
draft: false
tags:
---
  
## Use-case
Regularization ensures that the weights of the regression model aren't too large. This is important because large weights usually cause over-fitting which leads to poor performance on test data. It also prevents oscillation and introduces smoothness (*which is however an inductive bias in itself!*)
## Mathematically
The regularized error function is given by:

$$
\boxed{
\tilde{E}(\mathbf{w})=\overbrace{\frac{1}{2} \sum_{n=1}^N\left(y\left(x_n, \mathbf{w}\right)-t_n\right)^2}^\text{Sum of Squared Error}+\underbrace{\frac{\lambda}{2}\|\mathbf{w}\|^2}_\text{regularization}
}
$$


where,
- $\lambda\rightarrow$ balances the regularization term against the error term. It is different for each model.
- $1/2\rightarrow$ is the scaling factor that simplifies the derivative during optimization (calculating the gradient). 
![[Pasted image 20240418164715.png]]




