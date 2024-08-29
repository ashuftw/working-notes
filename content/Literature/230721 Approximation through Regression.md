---
title: Approximation through Regression
draft: false
tags:
---
  

For given *N* Data points

$$
\left(x_i, y_i\right), i=1, \ldots, N
$$


We search for a Regression Curve with *M* basis polynomials
	
$$
s(x)=\alpha_1 s_1(x)+\alpha_2 s_2(x)+\ldots+\alpha_M s_M(x)
$$

 Where $N\rightarrow$ is the number of data-points, $M\rightarrow$ points considered for regression 
## Quadratic Error 

$$
J(\mathbf{a})=\|\mathbf{y}-A \mathbf{a}\|_2^2
$$

Where, 
- Weights used to fit the regression model to the given function.
$$
\quad \mathbf{a}=\left(\begin{array}{c} \alpha_1 \\ \vdots \\ \alpha_M \end{array}\right) \in \mathbb{R}^M
$$
 
- Evaluation of the basis function at the given data points. 
$$
\quad A=\left(\begin{array}{ccc}s_1\left(x_1\right) & \cdots & s_M\left(x_1\right) \\ \vdots & & \vdots \\s_1\left(x_N\right) & \cdots & s_M\left(x_N\right)\end{array}\right) \in \mathbb{R}^{N \times M}
$$
 
	Note: The basis function for a polynomial regression is $s_i(x)=x^i$.  
- Is the dependent variable of the given data set. 
$$
\mathbf{y}=\left(\begin{array}{c} y_1 \\ \vdots \\ y_N\end{array}\right) \in \mathbb{R}^N
$$

[[230418 Regression]]
