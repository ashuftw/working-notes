  

## Continuity Equation

$$
\frac{\partial \rho}{\partial t}+\rho\,\nabla\cdot \vec u=0
$$


$$
\frac{\partial \rho}{\partial t}+\rho\left(\frac{\partial u}{\partial x}+\frac{\partial v}{\partial y}\right)=0
$$

## Momentum Equations
**In vector notation** 
$$
\rho \underbrace{\left(\frac{\partial \vec{u}}{\partial t}+\vec{u} \cdot \nabla \vec{u}\right)}_{\text {Acceleration }}=\underbrace{-\nabla p}_{\text {Pressure }}+\underbrace{\mu \Delta \vec{u}}_{\text {Viscosity }}
$$
or

$$
\rho \underbrace{\left(\frac{\partial \vec{u}}{\partial t}+\vec{u} \cdot \nabla \vec{u}\right)}_{\text {Acceleration }}=\underbrace{-\nabla p}_{\text {Pressure }}+\underbrace{\nabla \cdot\tau}_{\text {Shear Stress}}
$$


where $\tau=\left(\begin{array}{ccc}\tau_{x x} & \tau_{x y} & \tau_{x z} \\ \tau_{x y} & \tau_{y y} & \tau_{y z} \\ \tau_{x z} & \tau_{y z} & \tau_{z z}\end{array}\right)$

**In Leibniz notation (2D)**

$$
\begin{aligned}\rho\left(\frac{\partial u}{\partial t}+u \frac{\partial u}{\partial x}+v \frac{\partial u}{\partial y}\right) & =-\frac{\partial p}{\partial x}+\mu\left(\frac{\partial^2 u}{\partial x^2}+\frac{\partial^2 u}{\partial y^2}\right) \\\\
\rho\left(\frac{\partial u}{\partial t}+u \frac{\partial v}{\partial x}+v \frac{\partial v}{\partial y}\right) & =-\frac{\partial p}{\partial y}+\mu\left(\frac{\partial^2 v}{\partial x^2}+\frac{\partial^2 v}{\partial y^2}\right)\end{aligned}
$$


