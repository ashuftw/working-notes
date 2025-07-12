---
title: Quadrature Error
draft: false
tags: 
date: 2025-07-08
---

### Interpolation Error 

$$
f(x)=p(x)-r(x)
$$

where, 
- $f\rightarrow$ true function  
- $p\rightarrow$ approximating polynomial
- $r\rightarrow$ interpolation error error 

### Quadrature Error 

$$
\begin{align}
I(f)&=I(p)-I(r)\\& =Q(f)-\int_a^b r(x) \mathrm{d} x
\end{align}
$$

or 

$$
I(f)=Q(f)+\underbrace{C_1 h^2+C_2 h^4+C_3 h^6+\ldots}_\text{error term}
$$

where, 
- $I\rightarrow$ exact integral  
- $Q\rightarrow$ quadrature approximation 

## Some common Quadrature error expansions

#### Simple Left/Right Rectangle Rules ($q=1$)
$$
I(f)=Q_R(f)+C_1 h+C_2 h^2+C_3 h^3+\ldots
$$
These methods are not symmetric, so their error expansion includes all powers of $h$ , starting with an $O(h)$ term.
#### Summed Trapezoidal Rule / Summed Trapezoidal Rule ($q = 2$):
$$
I(f)=Q_T(f)+C_1 h^2+C_2 h^4+C_3 h^6+\ldots
$$
$O\left(h^2\right)$ term and proceeds in even powers. 
#### Simpson's rule ($q=4$)
$$
I(f)=Q_S(f)+C_1 h^4+C_2 h^6+C_3 h^8+\ldots
$$
The error for  starts at order $O\left(h^4\right)$. 

