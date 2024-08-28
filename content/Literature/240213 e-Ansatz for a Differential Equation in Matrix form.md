---
title: e-Ansatz for a Differential Equation in Matrix form
draft: false
tags:
---
  

### Linear differential equation 

$$
\bar q^{\prime}(t)=A \bar q(t)
$$

### e-ansatz  

$$
\boxed{\bar q(t)=e^{\lambda t} \bar v}
$$

where $q(t)$ is a vector-valued function of time, $\lambda$ is a scalar (possibly complex), and $v$ is a constant vector.

The *ansatz*  $q(t)$ is a solution is a solution if $\lambda$ is an **eigenvalue** of $A$ and $v$ is the corresponding **eigenvector**. 
> Note: By definition $A v=\lambda v$

For a diagonizable matrix $A$,  
$$
A=V \Lambda V^{-1}
$$

Where, 
- $\Lambda$  is a diagonal matrix with eigenvalues $\lambda_1, \lambda_2, \ldots, \lambda_n$ on the diagonal.
- $V$ matrix whose columns are the corresponding eigenvectors of $A$.

