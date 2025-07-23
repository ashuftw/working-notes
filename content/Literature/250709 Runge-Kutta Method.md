---
title: Runge-Kutta Method
draft: false
tags: 
date: 2025-07-09
---
## General Procedure

A [[250708 Butcher Table|Butcher Table]] for a Runge-Kutta method with $s$ stages has the form:

$$
\begin{array}{c|c}
\mathbf{c} & A \\
\hline
& \mathbf{b}^T
\end{array}
=
\begin{array}{c|cccc}
c_1 & a_{11} & a_{12} & \cdots & a_{1s} \\
c_2 & a_{21} & a_{22} & \cdots & a_{2s} \\
\vdots & \vdots & \vdots & \ddots & \vdots \\
c_s & a_{s1} & a_{s2} & \cdots & a_{ss} \\
\hline
& b_1 & b_2 & \cdots & b_s
\end{array}
$$

The procedure to find $y_{n+1}$ from $y_n$ is:

**1. Calculate Intermediate Stages:**

$$
q_i = h \cdot f\left(t_n + c_i h, y_n + \sum_{j=1}^{s} a_{ij} q_j\right) \quad \text{for } i = 1, \dots, s
$$


**2. Calculate Final Step:**

$$
y_{n+1} = y_n + \sum_{i=1}^{s} b_i q_i
$$


---
## Examples
### (i) A Two-Stage Implicit Method


$$
\begin{array}{c|cc}
0 & 1/3 & 1/3 \\
2/3 & 0 & 2/3 \\
\hline
& 1/4 & 3/4
\end{array}
$$

**Procedure:**
1.  **Stage 1:**
	
$$
q_1 = h \cdot f\left((t_n + c_1 h), (y_n +  a_{11} q_1+a_{12}q_2+a_{13}q_3+...)\right)
$$

    
$$
q_1 = h \cdot f\left(t_n, y_n + \frac{1}{3}q_1 + \frac{1}{3}q_2\right)
$$

2.  **Stage 2:**
    
$$
q_2 = h \cdot f\left(t_n + \frac{2}{3}h, y_n + \frac{2}{3}q_2\right)
$$

3.  **Final Result:**
	
$$
y_{n+1} = y_n + b_1 q_1+b_2 q_2+...
$$

    
$$
y_{n+1} = y_n + \frac{1}{4}q_1 + \frac{3}{4}q_2
$$


### (ii) Implicit Midpoint Rule


$$
\begin{array}{c|c}
1/2 & 1/2 \\
\hline
& 1
\end{array}
$$

**Procedure:**
1.  **Stage 1:**
    
$$
q_1 = h \cdot f\left(t_n + \frac{1}{2}h, y_n + \frac{1}{2}q_1\right)
$$

2.  **Final Result:**
    
$$
y_{n+1} = y_n + q_1
$$


### (iii) A Three-Stage Explicit Method


$$
\begin{array}{c|ccc}
0 & 0 & 0 & 0 \\
1 & 1 & 0 & 0 \\
1/2 & 1/4 & 1/4 & 0 \\
\hline
& 1/6 & 1/6 & 2/3
\end{array}
$$


**Procedure:**
1.  **Stage 1:**
    
$$
q_1 = h \cdot f(t_n, y_n)
$$

2.  **Stage 2:**
    
$$
q_2 = h \cdot f(t_n + h, y_n + q_1)
$$

3.  **Stage 3:**
    
$$
q_3 = h \cdot f\left(t_n + \frac{1}{2}h, y_n + \frac{1}{4}q_1 + \frac{1}{4}q_2\right)
$$

4.  **Final Result:**
    
$$
y_{n+1} = y_n + \frac{1}{6}q_1 + \frac{1}{6}q_2 + \frac{2}{3}q_3
$$

    
## Rule of thumb to determine if procedure is explicit or implicit.
- **Explicit** if the Butcher tableau has zeros on and above the main diagonal (lower triangular with zero diagonal)
- **Implicit** if there are non-zero entries on or above the main diagonal
### Examples
1. **Explicit: Euler-Heun Method**
	The Butcher tableau for the Euler-Heun method is:
	
$$
\begin{array}{c|cc}
	0 & 0 & 0 \\
	1 & 1 & 0 \\
	\hline
	& 1/2 & 1/2
	\end{array}
$$

	The coefficient matrix is $A = \begin{pmatrix} 0 & 0 \\ 1 & 0 \end{pmatrix}$. Since all entries on and above the main diagonal are zero, the method is **explicit**.
2. **Implicit: Crank-Nicolson Method**
	The Butcher tableau for the Crank-Nicolson method is:
	
$$
\begin{array}{c|cc}
	0 & 0 & 0 \\
	1 & 1/2 & 1/2 \\
	\hline
	& 1/2 & 1/2
	\end{array}
$$

	The coefficient matrix is $A = \begin{pmatrix} 0 & 0 \\ 1/2 & 1/2 \end{pmatrix}$. Because there is a non-zero entry on the main diagonal ($a_{22} = 1/2$), the method is **implicit**. The calculation for the second stage depends on itself, which requires solving an equation.