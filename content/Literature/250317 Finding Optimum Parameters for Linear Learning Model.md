---
title: Finding Optimum Parameters for Linear Learning Model
draft: false
tags: 
date: 2025-03-17
---
For a linear model $y(x, w)=w^T \phi(x)$ with squared error function:


$$
E(w)=\frac{1}{2} \sum_{n=1}^N\left(t_n-w^T \phi\left(x_n\right)\right)^2
$$


The optimal parameters $w^*$ are found by:
1. Setting the gradient to zero: $\nabla E(w)=0$
2. Solving the resulting equation

**Simplification**
Write in matrix form (where $\Phi$ is the [[250623 Design matrix|Design matrix]])


$$
E(w)=\frac{1}{2}\|t-\Phi w\|^2
$$


Setting Gradient to zero


$$
\nabla_w E(w)=-\Phi^T(t-\Phi w)=0
$$


Solve for $w$: 


$$
\Phi^T \Phi w=\Phi^T t
$$


 The optimal parameter vector is: 

 
$$
w^*=\left(\Phi^T \Phi\right)^{-1} \Phi^T t
$$


 For the regularized case (MAP estimation):


$$
w_{M A P}=\left(\lambda I+\Phi^T \Phi\right)^{-1} \Phi^T t
$$


Where $\lambda$ is the regularization parameter.

