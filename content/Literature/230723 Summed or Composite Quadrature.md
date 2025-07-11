---
title: Summed or Composite Quadrature
draft: false
date: 2023-07-23
---
It is a [[230507 Quadrature - Derivation and Formulae|Quadrature]] where the domain $x\in[a,b]$ is split into multiple grid points $j=0,1,2\dots J$ with $a = x_0 < x_1 < \dots < x_J = b$


$$
\boxed{
\int_a^b f(x) \mathrm{d} x=\sum_{j=0}^{J-1} \int_{x_j}^{x_{j+1}} f(x)\ \mathrm{d}x
}
$$


We sum only till $(J-1)$ because $j=J$ is the end point which means the substitution $x_{J+1}$ doesn't exist.  

![[../Files/Pasted image 20250710102033.png|center|600]]
## Comparison of Quadrature Rules and their Composite form

| Quadrature rule | Composite Quadrature                                                                         | Fixed Step                                                                                                               |
| --------------- | -------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| Left Rectangle  | $\sum_{j=0}^{J-1}f\left(x_j\right)\left(x_{j+1}-x_j\right)$                                  | $h\sum_{j=0}^{J-1}f\left(x_j\right)$                                                                                     |
|                 |                                                                                              |                                                                                                                          |
| Midpoint        | $\sum_{j=0}^{J-1}f\left(\frac{x_{j+1}+x_j}{2}\right)\left(x_{j+1}-x_j\right)$                | $h \sum_{j=0}^{J-1} f\left(\frac{x_{j+1}+x_j}{2}\right)$                                                                 |
|                 |                                                                                              |                                                                                                                          |
| Trapezoid       | $\sum_{j=0}^{J-1}\left(x_{j+1}-x_j\right) \frac{f\left(x_j\right)+f\left(x_{j+1}\right)}{2}$ | $\frac{h}{2} \sum_{j=0}^{J-1}\left(f\left(x_j\right)+f\left(x_{j+1}\right)\right)$                                       |
| Simpson's       |                                                                                              | $\frac{h}{6} \sum_{j=0}^{J-1}\left(f\left(x_j\right)+4 f\left(\frac{x_j+x_{j+1}}{2}\right)+f\left(x_{j+1}\right)\right)$ |