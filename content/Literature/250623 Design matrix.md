---
title: Design Matrix
draft: false
tags: 
date: 2025-06-23
---
The design matrix $\Phi$ is an $N \times M$ matrix where each row contains the basis function values for one data point:



$$
\Phi = \begin{pmatrix} 
\phi(x_1)^T \\ 
\phi(x_2)^T \\ 
\vdots \\ 
\phi(x_N)^T 
\end{pmatrix} = \begin{pmatrix} 
\phi_0(x_1) & \phi_1(x_1) & \cdots & \phi_{M-1}(x_1) \\ 
\phi_0(x_2) & \phi_1(x_2) & \cdots & \phi_{M-1}(x_2) \\ 
\vdots & \vdots & \ddots & \vdots \\ 
\phi_0(x_N) & \phi_1(x_N) & \cdots & \phi_{M-1}(x_N) 
\end{pmatrix}
$$



This allows us to write all predictions compactly as $\Phi w$ instead of computing $w^T\phi(x_n)$ for each point individually.


