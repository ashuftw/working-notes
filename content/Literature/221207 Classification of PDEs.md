Status: #finished 

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

In Multi-index notation
![](http://127.0.0.1:43607/paste-e16d8220de1aebdd002eb92586d741ea9be3bbe6.png)

1. **Elliptic**: $\lambda_{ij}$ do not vanish and have the same sign.
$$
\begin{equation}
A_{ij}=\begin{pmatrix}1 &0& 0\\ 0 &1& 0\\0& 0& 1
\end{pmatrix}
\end{equation}
$$

2. **Parabolic**: One Eigen Value Vanishes.
$$
\begin{equation}
A_{ij}=\begin{pmatrix}0 &0& 0\\ 0 &1& 0\\0& 0& 1
\end{pmatrix}
\end{equation}
$$

3. Hyperbolic: Eigen Values don't vanish and 1 of the eigen values have a different sign.
$$
\begin{equation}
A_{ij}=\begin{pmatrix}-1 &0& 0\\ 0 &1& 0\\0& 0& 1
\end{pmatrix}
\end{equation}
$$

---
# References
1. https://books.physics.oregonstate.edu/LinAlg/pdeclass.html
