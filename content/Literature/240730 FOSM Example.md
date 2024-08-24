---
title: FOSM Example
draft: false
tags:
---
FOSM (First order second moment) for a measurement problem. Many quantities can only be measured indirectly. In these cases a measurement model
$$
Z=g\left(X_1, X_2, \ldots, X_M\right)
$$
is used, which connects the observable quantities $\boldsymbol{X}=\left(X_1, X_2, \ldots, X_M\right)^{\top}$ with the not directly observable quantity $Z$. Erroneous measurements of $\boldsymbol{X}$ then lead to deviations in $Z$.

Consider the example of an electrical resistor whose resistance depends on the temperature. We denote with $V, \bar{R}, \alpha, T, \bar{T}$ the voltage, the resistance at $\bar{T}$, the linear coefficient of temperature, the current temperature and the reference temperature. For the measurement model there holds
$$
P=g(V, \alpha, T)=\frac{V^2}{\bar{R}(1+\alpha(T-\bar{T}))}
$$
where $P$ denotes power.
Use FOSM to find an approximation of the standard deviation of $P$, i.e. $\sigma_P$, in dependence of the known uncertainties of the directly observable quantities
$$
\begin{aligned}
& V \sim \mathcal{N}\left(\mu_V, \sigma_V\right) \\
& \alpha \sim \mathcal{U}\left(\bar{\alpha}-\Delta_\alpha, \bar{\alpha}+\Delta_\alpha\right) \\
& T \sim \mathcal{U}\left(\bar{T}-\Delta_T, \bar{T}+\Delta_T\right)
\end{aligned}
$$

All parameters of the given distributions as well as $\bar{R}$ can be considered

![[../../Private/Excalidraw/Drawing 2024-07-30 17.25.16.excalidraw#^group=nSz2VEPPlQ4GSo9kdkIiA|1000]]

