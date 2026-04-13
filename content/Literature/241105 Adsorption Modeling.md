---
title: Adsorption Modeling
draft: true
tags: 
date: 2024-11-05
---
### Boundary condition



$$
-D_{AB}\left(\frac{\partial C_A}{\partial y}\right)_{y=W} = \dot{q}(t)
$$



# Forward Difference



$$
-D_{AB}\frac{C_0 - C_1}{\Delta y} = \text{flux}
$$





$$
C_0 = C_1- \Delta y \cdot \frac {\text{flux}}{D_{AB}}
$$



Note: 
- $j=0\rightarrow$ Ghost layer 
- $j=1\rightarrow$ Physical wall
![[../Files/Pasted image 20241106133251.png|center|400]]
The wall lies in between the Ghost layer and the Inner layer. Therefore $\Delta y$ is divided by $2$



$$
\boxed{
C_0 = C_1- \frac {\Delta y} 2 \cdot \frac {\text{flux}}{D_{AB}} 
}
$$



# 3-Point Stencil

### Taylor series expansion for points near wall $(j=0)$:



$$
C_A(j+1) = C_A(j) + \Delta y\left(\frac{\partial C_A}{\partial y}\right) + \frac{(\Delta y)^2}{2}\left(\frac{\partial^2 C_A}{\partial y^2}\right) + O(\Delta y^3)
$$





$$
C_A(j+2) = C_A(j) + 2\Delta y\left(\frac{\partial C_A}{\partial y}\right) + 2(\Delta y)^2\left(\frac{\partial^2 C_A}{\partial y^2}\right) + O(\Delta y^3)
$$

Using Subscript notation

$$
C_1 = C_0 + \Delta y\left(\frac{\partial C_A}{\partial y}\right)_0 + \frac{(\Delta y)^2}{2}\left(\frac{\partial^2 C_A}{\partial y^2}\right)_0
$$





$$
C_2 = C_0 + 2\Delta y\left(\frac{\partial C_A}{\partial y}\right)_0 + 2(\Delta y)^2\left(\frac{\partial^2 C_A}{\partial y^2}\right)_0
$$



### Eliminate higher order terms

**Multiply first equation by 4 and subtract second equation**



$$
\begin{align}
4C_1 - C_2 = 4\left[C_0 + \Delta y\left(\frac{\partial C_A}{\partial y}\right)_0 + \frac{(\Delta y)^2}{2}\left(\frac{\partial^2 C_A}{\partial y^2}\right)_0\right] \\
- \left[C_0 + 2\Delta y\left(\frac{\partial C_A}{\partial y}\right)_0 + 2(\Delta y)^2\left(\frac{\partial^2 C_A}{\partial y^2}\right)_0\right]
\end{align}
$$



**Simplify**



$$
4C_1 - C_2 = 3C_0 + 2\Delta y\left(\frac{\partial C_A}{\partial y}\right)_0
$$



**From boundary condition**



$$
\left(\frac{\partial C_A}{\partial y}\right)_0 = -\frac{\dot{q}}{D_{AB}} = -\frac{\text{flux}}{D_{AB}}
$$



**Substituting**



$$
4C_1 - C_2 = 3C_0 - 2\Delta y\frac{\text{flux}}{D_{AB}}
$$



**Rearranging**



$$
C_0 = \frac{4C_1 - C_2 + 2\Delta y\frac{\text{flux}}{D_{AB}}}{3}
$$

---
# TSA Physics: Temperature-Dependent Adsorption

## Core Equations

**Species transport (LDF model):**

$$\frac{dq}{dt} = k_s (q_e - q)$$

- $k_s$ — kinetic rate constant, assumed constant
- $q$ — current adsorbed loading on sorbent [mol/kg]
- $q_e$ — equilibrium loading at current conditions [mol/kg]

The sign of $(q_e - q)$ determines direction:
- $(q_e - q) > 0$ → adsorption
- $(q_e - q) < 0$ → desorption (regeneration)

---

## Equilibrium Loading — Toth Isotherm

$q_e$ is not constant. It is computed at every point from the Toth isotherm:

$$q_e = \frac{n_s \, b \, p_{CO_2}}{\left(1 + (b \, p_{CO_2})^{t_T}\right)^{1/t_T}}$$

where $p_{CO_2}$ is the local CO₂ partial pressure and $n_s$, $b$, $t_T$ are temperature-dependent parameters.

---

## Temperature Dependence of Toth Parameters

**Adsorption affinity** (Van't Hoff):

$$b(T) = b_0 \exp\!\left(\frac{\Delta H_0}{R T_0}\left(\frac{T_0}{T} - 1\right)\right)$$

**Saturation capacity:**

$$n_s(T) = n_{s0} \exp\!\left(\chi\left(1 - \frac{T}{T_0}\right)\right)$$

**Toth exponent:**

$$t_T(T) = t_{T0} + \alpha\left(1 - \frac{T_0}{T}\right)$$

where $T_0$ is the reference temperature and $\Delta H_0$, $\chi$, $\alpha$ are fitted material constants.

---

## Partial Pressure

$$p_{CO_2} = C_A \cdot R \cdot T$$

where $C_A$ is the local molar concentration of CO₂ from the transport equation.

---

## Physical Interpretation for TSA

| Phase | Temperature | $q_e$ | Driving force $(q_e - q)$ | Result |
|-------|-------------|-------|--------------------------|--------|
| Adsorption | Low (ambient) | High | Positive | CO₂ captured |
| Regeneration | High | Low | Negative | CO₂ released |

The same LDF equation governs both phases. No special casing is needed.