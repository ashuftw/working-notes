---
title: Gradient Descent
draft: true
tags: 
date: 2025-03-18
---

The learning rule for gradient descent is

$$
w_{k+1}=w_k-\eta \nabla E(w)
$$

Where:

- $w_k$ is the parameter vector at iteration $k$
- $w_{k+1}$ is the updated parameter vector for the next iteration
- $\eta$ is the learning rate (a positive scalar value)
- $\nabla E(w)$ is the gradient of the error function with respect to parameters $w$

This iterative update rule moves the parameters in the direction of steepest descent of the error function, with the step size controlled by the learning rate $\eta$. The process continues until the gradient becomes approximately zero ($\nabla E(w) \approx 0$) or some other stopping criterion is met.