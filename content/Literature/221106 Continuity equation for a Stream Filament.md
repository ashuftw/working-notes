---
title: Continuity equation for a Stream Filament
draft: false
date: 2022-11-06
---

![[Pasted image 20221106141239.png|center|350]]

For a Stream element

$$
\text{Flow rate}=\text{Rate of Mass entering - Rate of mass leaving}
$$



$$
\frac{dm}{dt}=\dot m_1 -\dot m_2 \tag 1
$$

Stream element extends from $s$ to $s+ds$  and the location is given by $z(s)$
Naturally all the flow properties $(v, p,\rho)$ are functions of $(s,t)$

Mass flux through left face

$$
\dot m_1=\rho\cdot A\cdot v \tag{2}
$$

Using the [[231115  The Taylor Expansion|The Taylor Expansion]] $(x=ds,a=0)$ Mass flux through right face can be approximated to.  

$$
\begin{aligned}
\dot m_2&=\left(\rho+\frac{\partial\rho}{\partial s}ds\right)\cdot \left(A+\frac{\partial A}{\partial s}ds\right)\cdot \left(v+\frac{\partial v}{\partial s}ds\right)
\end{aligned}\tag{3}
$$

Ignoring higher order terms ($ds\cdot ds$ terms are ~ $0$) 

$$
\begin{aligned}
&= \rho Av+\left(Av\frac{\partial \rho}{\partial s}+\rho A\frac{\partial v}{\partial s}+\rho v\dfrac{\partial A}{\partial s} \right)ds+...
\end{aligned}\tag{4}
$$

Applying reverse chain rule 

$$
\begin{aligned}
&= \rho Av+\frac{\partial (\rho A v)}{\partial s}ds 
\end{aligned}\tag{5}
$$

Flow rate $\dot m$ can be expressed as 

$$
\frac{\partial m}{\partial t } = \dfrac{\partial (\rho \cdot dv)}{\partial t} = \dfrac{\partial \rho}{\partial t}\cdot A\cdot ds\tag 6
$$

Substituting values of  $\dot m, m_1$ & $m_2$ in $(1)$

$$
\dfrac{\partial \rho}{\partial t}\cdot A\cdot ds= \rho A v-\left(
\rho Av+\frac{\partial (\rho A v)}{\partial s}ds \right)
\tag{7}
$$


Subsequently 

$$
\boxed{
\dfrac{\partial \rho}{\partial t}+\frac{1}{A}\cdot \frac{\partial (\rho A v)}{\partial s} =0
} \tag{8}
$$

Gives the Continuity equation for a 1 Dimensional Compressible flow in a Stream Filament. 

## Application
1. **Compressible Steady Flow**
	
$$
\boxed{
	\rho A v = \text{const}
   }
$$


2. **Unsteady Incompressible Flow**
	
$$
\boxed{
	Av= \text{const}=f(t)
	}
$$

3. **Steady Incompressible Flow**
	
$$
\boxed{
	Av=\text{const}
	}
$$


