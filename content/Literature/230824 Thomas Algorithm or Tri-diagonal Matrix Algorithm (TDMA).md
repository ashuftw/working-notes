---
title: Thomas Algorithm or Tri-diagonal Matrix Algorithm (TDMA)
draft: false
tags:
---
## Definition
The Thomas Algorithm is used to solve a linear [[230824 Tridiagonal matrix|Tridiagonal matrix]]

## Linear Tridiagonal Matrix
We have the system of linear equations

$$
\begin{align}
a_1 x_1 + c_1 x_2 &= b_1 \\
b_2 x_1 + a_2 x_2 + c_2 x_3 &= b_2 \\
&\vdots \\
b_{n-1} x_{n-2} + a_{n-1} x_{n-1} + c_{n-1} x_n &= b_{n-1} \\
b_n x_{n-1} + a_n x_n &= b_n
\end{align}
$$

In Matrix form 

$$
\begin{pmatrix}
a_1 & c_1 & & & \\
b_2 & a_2 & c_2 & & \\
& \ddots & \ddots & \ddots & \\
& & \ddots & \ddots & c_{n-1} \\
& & & b_n & a_n
\end{pmatrix}
\begin{pmatrix}
x_1 \\
x_2 \\
x_3 \\
\vdots \\
x_n
\end{pmatrix}
=
\begin{pmatrix}
b_1 \\
b_2 \\
b_3 \\
\vdots \\
b_n
\end{pmatrix}
$$

If $A$ is the TDM, $x$ is the vector containing the unknowns and $b$ is the vector containing constants, we have

$$
{Ax=b}
$$

## LU Decomposition
We consider the factorization

$$
A=L U
$$

where $L,U \rightarrow$ Lower and Upper Triangular Matrix respectively.

$$
L=\left(\begin{array}{ccccc}
1 & & & & \\
\ell_2 & 1 & & & \\
& \ddots & \ddots & & \\
& & \ddots & \ddots & \\
& & & \ell_n & 1
\end{array}\right), \quad U=\left(\begin{array}{ccccc}
r_1 & s_1 & & & \\
& r_2 & s_2 & & \\
& & \ddots & \ddots & \\
& & & \ddots & s_{n-1} \\
& & & & r_n
\end{array}\right)
$$

Then, we need to determine $\ell_2, \ldots, \ell_n, r_1, \ldots, r_n$ and $s_1, \ldots, s_{n-1}$.
## Formulas that can derived
Given that $r_i\ne0$,  $i=1, \ldots n-1$
- for $i=1, \ldots n-1$
	
$$
\begin{aligned}
& s_i=c_i\\
& r_1=a_1
\end{aligned}
$$

- for $i=2, \ldots n$
	
$$
\begin{aligned}
-\ell_i & =\frac{b_i}{r_{i-1}} \\
-r_i & =a_i-\ell_i s_{i-1}
\end{aligned}
$$

