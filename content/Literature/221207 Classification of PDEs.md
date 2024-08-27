---
title: Classification of PDEs
draft: false
tags:
---
  

A general 2$^\text{nd}$ order PDE
$$
\mathcal{L}\psi = b
$$
 Where $\mathcal L\psi$ is given by
$$
\mathcal{L} \psi=\sum_{i,j=1}^4 A_{ij}(x_k) 
{\partial^2\psi\over\partial x_i\partial x_j}
+\sum_{i=1}^4 B_i(x_k) {\partial \psi\over\partial x_i} + C(x_k)
$$

$b$ is a source term

1. **Elliptic**: $\lambda_{ij}$ do not vanish and have the same sign.
$$
A_{ij}=\begin{pmatrix}1 &0& 0\\ 0 &1& 0\\0& 0& 1
\end{pmatrix}
$$

2. **Parabolic**: One Eigen Value Vanishes.
$$
A_{ij}=\begin{pmatrix}0 &0& 0\\ 0 &1& 0\\0& 0& 1
\end{pmatrix}
$$

3. Hyperbolic: Eigen Values don't vanish and 1 of the eigen values have a different sign.
$$
A_{ij}=\begin{pmatrix}-1 &0& 0\\ 0 &1& 0\\0& 0& 1
\end{pmatrix}
$$

---
# References
1. https://books.physics.oregonstate.edu/LinAlg/pdeclass.html
