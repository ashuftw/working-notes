  
## Formula  

$$
\lambda_{1,2}=m \pm \sqrt{m^2-p}
$$


Where $m \rightarrow$ Mean of the Eigen Values (diagonal) and $p \rightarrow$ product of the Eigen Values (determinant)
## Example
**Matrix**

$$
\left[\begin{array}{ll}
3 & 1 \\
4 & 1
\end{array}\right]
$$

*Mean* $m=2$
*Product* $p=3-4=-1$
**Eigenvalues**

$$
\boxed{\Rightarrow \lambda_1, \lambda_2=2 \pm \sqrt{5}}
$$



---
Eigenvectors:
Once we have the eigenvalues of a given matrix, find the eigenvectors by solving:

$$
A \vec{v}=\lambda \vec{v}
$$

which is equivalent to:

$$
\begin{gathered}
(\boldsymbol{A}-\lambda \boldsymbol{I}) \overrightarrow{\boldsymbol{v}}=\overrightarrow{\mathbf{0}} \\
\text { or } \\
(\lambda \boldsymbol{I}-\boldsymbol{A}) \overrightarrow{\boldsymbol{v}}=\overrightarrow{\mathbf{0}}
\end{gathered}
$$


The eigen vector can be found out by solving the matrix system. (Note: Here $\vec{v}=v_1 v_2$)




