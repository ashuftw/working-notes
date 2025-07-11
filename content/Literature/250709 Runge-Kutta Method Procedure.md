---
title: Runge-Kutta Method Procedure
draft: false
tags: 
date: 2025-07-09
---
### General form of [[250708 Butcher Table|Butcher Table]]

$$
\begin{array}{c|cc}
& C_1 & a_{11} & a_{21} \\
& C_2 & a_{21} & a_{21} \\
\hline
& & b_1 & b_2
\end{array}
$$

### Intermediate stages

$$
k_i=f(t_n+  c_i h, y_n+h \sum a_{i j} k_j)
$$

**Example:**
-	**Stage 1**

$$
k_1=f\left(t_n+c_1 h, \quad y_n+h\left(a_{11} k_1+a_{12} k_2\right)\right)
$$

- **Stage 2**
	
$$
k_2=f\left(t_n+c_2 h, \quad y_n+h\left(a_{21} k_1+a_{22} k_2\right)\right)
$$

### Finalizing Solution

$$
y_{n+1}=y_n+h \sum b_i k_i
$$

**Example**

$$
y_{n+1}=y_n+h\left(\frac{3}{4} k_1+\frac{1}{4} k_2\right)
$$


### Rule of thumb to determine if procedure is explicit or implicit.
- **Explicit** if the Butcher tableau has zeros on and above the main diagonal (lower triangular with zero diagonal)
- **Implicit** if there are non-zero entries on or above the main diagonal



 