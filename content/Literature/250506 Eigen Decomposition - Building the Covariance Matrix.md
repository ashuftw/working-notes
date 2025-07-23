---
title: Eigen Decomposition - Building the Covariance Matrix
draft: false
tags: 
date: 2025-05-06
---
For a [[content/Literature/230516 Covariance|Covariance]] matrix $C_X$, we want to find:



$$
C_X=V E V^T
$$



Where:
- $E$ is a diagonal matrix containing the eigenvalues
- $V$ is a matrix whose columns are the corresponding eigenvectors

## Steps

1. Finding eigenvalues: We solve the characteristic equation $\operatorname{det}\left(C_X-\lambda I\right)=0$ to find values of $\lambda$ (eigenvalues).
2. Finding eigenvectors: For each eigenvalue $\lambda_i$, we solve $\left(C_X-\lambda_i I\right) v_i=0$ to find the corresponding eigenvector $v_i$.
3. Building matrices:
- $E$ is a diagonal matrix with eigenvalues $\lambda_i$ on the diagonal
- $V$ is a matrix with eigenvectors $v_i$ as columns
