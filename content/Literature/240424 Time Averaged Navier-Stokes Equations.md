---
title: Time Averaged Navier-Stokes Equations
draft: false
tags: 
date: 2024-04-04
---
## NS into RANS
$$
\begin{gathered}
\frac{\partial u_i}{\partial t}+\frac{\partial \boldsymbol{u}_{\boldsymbol{i}} \boldsymbol{u}_{\boldsymbol{j}}}{\boldsymbol{\partial} \boldsymbol{x}_{\boldsymbol{j}}}=-\frac{1}{\rho} \frac{\partial p}{\partial x_i}+v \frac{\partial^2 u_i}{\partial x_j^2}+g_i \\
\frac{\partial \bar{u}_i}{\partial t}+\frac{\partial \bar{u}_i \overline{\boldsymbol{u}}_{\boldsymbol{j}}}{\boldsymbol{\partial} \boldsymbol{x}_{\boldsymbol{j}}}+\frac{\partial \overline{\boldsymbol{u}_{\boldsymbol{i}}^{\prime} \boldsymbol{u}_{\boldsymbol{j}}^{\prime}}}{\boldsymbol{\partial} \boldsymbol{x}_{\boldsymbol{j}}}=-\frac{1}{\rho} \frac{\partial \bar{p}}{\partial x_i}+v \frac{\partial^2 \bar{u}_i}{\partial x_j^2}+\bar{g}_i
\end{gathered}
$$
**Note**
- The variables are split into a mean and a fluctuating component.
$$
\begin{aligned}
v_i & =\bar{v}_i+v_i^{\prime} \\
p & =\bar{p}+p^{\prime}
\end{aligned}
$$
- These equations are substituted into the NS and then the equation is Time Averaged.
- To remember:
$$
\begin{aligned}
& \overline{\bar{v}}_i \bar{v}_j=\bar{v}_i \bar{v}_j \\
& \overline{\bar{v}_i v_j^{\prime}}=\overline{\bar{v}}_i \bar{v}_j^{\prime}=0 \text { and } \overline{\bar{v}_j v_i^{\prime}}=\overline{\bar{v}}_j \bar{v}_i^{\prime}=0
\end{aligned}
$$

---
# References
- **Full derivation**: Chalmers, Turbulence Modeling Pg. 82