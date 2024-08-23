Status: #finished  
## Lemma
The gradient gives the direction of the largest directional derivative, hence it points to the direction of the steepest slope.

## Proof
The [[231205 Directional Derivative|Directional Derivative]] of a vector function is given by. 
$$
\begin{aligned}
\frac{\partial}{\partial \vec{n}} u(\vec{x}) & =\vec{n} \cdot \nabla u(\vec{x}) \\
& =\|\vec{n}\|_2 \cdot\|\nabla u(\vec{x})\|_2 \cdot \cos \theta
\end{aligned}
$$
where $\theta$ is the angle between the two vectors. i.e $\cos \angle(\nabla u, \mathbf{n})$
The largest directional derivative is given by
$$
\begin{aligned}
\max \left(\frac{\partial}{\partial \vec{n}} u(\vec{x})\right) & =\max \left(\|\vec{n}\|_2 \cdot\|\nabla u(\vec{x})\|_2 \cdot \cos \theta\right) \\
& =1 \cdot\|\nabla u(\vec{x})\|_2 \cdot 1 \\
& =\|\nabla u(\vec{x})\|_2
\end{aligned}
$$

RHS is maximum when $\cos \theta=1, \Rightarrow \theta=0$. This means that the angle between the Direction of derivative and the Gradient is 0 .
$\therefore$ Thus the direction of the gradient is the same as the direction of the steepest slope (Because of the maximizing function)






---
# References
