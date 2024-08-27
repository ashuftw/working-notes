 #abandoned 

Tags: [[CFD]] [[Meshing]]

# MRF framework for Turbomachinery [^1]
### Definitions:
* **Axis of rotation ($s$)**: 
$$
s=x_2-x_1
$$

	Where $x_1$ and $x_2$ are any two points on the axis.
* **Rotation Vector ($\Omega$):**
$$
\Omega =\omega\cdot s
$$

	Where $\omega\rightarrow$ rotational speed 
* **Distance Vector ($r$):** 
$$
r=x_p-x_o
$$

	Where $x_p \rightarrow$ cell centroid, $x_o\rightarrow$ axis of rotation
	Note: $r$ is unique to each cell in the mesh
- **Relative Velocity ($U_r$)**:
![[Pasted image 20220605170117.png|750]]

#### Derivation
Velocity in a frame rotating with the blade
$$
\begin{align}U&= U_r+\Omega\times r\end{align}\tag{1}
$$

Incompressible Navier-Stokes equations
$$
\begin{align}\nabla\cdot (U\ U) &=-\dfrac{1}{\rho}\nabla p +\nabla \cdot(\nu\ \nabla U)\end{align}\tag{2}
$$

After substitution and simplification,[^2] we have 
**Single Reference Frame (Frame)**
$$
\begin{align}\nabla\cdot (U_r\ U_r) &=-\nabla p +\nabla \cdot(\nu\ \nabla U_r)-\underbrace{\Omega\times\Omega\times r}_\text{Centrifugal}-\underbrace{2\Omega\times U_r}_\text{Coriolis}\end{align}
$$

- We end up with two source terms for the Centrifugal and Coriolis forces
- Unknown is now the relative velocity, $U_r$
- $U$ is calculated as a post-processing operation:
$$
U=U_r+\Omega\times r
$$

**Multiple Reference Frames**
![[Pasted image 20220608111755.png|600]]

$$
\nabla\cdot(U\ U_r)=-\nabla p+\nabla\cdot(\nu \ \nabla U)-\Omega \times U
$$



---
# References
[^1]: https://www.youtube.com/watch?v=oa-xcE0_0UY
[^2]: https://openfoamwiki.net/index.php/See_the_MRF_development 
[^3]: https://www.afs.enea.it/project/neptunius/docs/fluent/html/ug/node370.htm