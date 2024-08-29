---
title: Lagrange interpolation
draft: false
tags:
---
   

The Lagrange interpolation defines a polynomial at each point. The Polynomial interpolating the entire data set is the sum of the product of value of the function $y_i$ at that point and individual polynomial calculated at that point. 
- **Lagrangian Basis polynomials, $L_i(x)$:**
	
$$
L_n^N\left(x_i\right)=\prod_{\substack{j=0 \\ j \neq n}}^N \frac{x_i-x_j}{x_n-x_j}= \begin{cases}0, & \text { for } i \neq n \\ 1, & \text { for } i=n\end{cases}
$$

- **Lagrange interpolation Polynomial, $P(x)$:**
	
$$
p(x)=\sum_{n=0}^N y_n L_n^N(x)
$$


Note: 
- $n$ -> is the Order of the Polynomial. 
- $(n+1)$ -> Interpolation points.



