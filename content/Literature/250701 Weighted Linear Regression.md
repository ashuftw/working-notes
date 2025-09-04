---
title: Weighted Linear Regression
draft: true
tags: 
date: 2025-07-01
---

Weighted Linear Regression assigns weights to different data points in order to mark their importance. 

**Gaussian Weighted Linear Regression**
Here the importance of the data points (weights) is specified as a distribution around the center (Gaussian). This creates a localized regression which fits more closely with specified regions of data. 

![[../Files/Pasted image 20250701141206.png|800]]
The weight is distributed using the Gaussian 
![[../Files/Pasted image 20250701143529.png|center|500]]
### Solution for Weighted Linear Regression
**Weighted Squared Error**


$$
E(w)=\frac{1}{2} \sum_{n=1}^Nd_n\left(y\left(x_n, w\right)-t_n\right)^2
$$


where $d_n$ is the weight at a point $n$

**Solution**
1. Form diagonal weight matrix $D$ where $D_{nn} = d_n$
2. Apply weighted [[250701 Ordinary Least squares Solution|least squares]] formula:




	$$
	\boxed{
	w* = (\Phi^T D \Phi)^{-1}\Phi^T D T
	}
	$$




where:

$$
D=\left(\begin{array}{ccc} d_1 & \ldots & \\ \vdots & \ddots & \vdots \\ & \ldots & d_n \end{array}\right)
$$

- $D$ = weight matrix 
- $X$ = design matrix (data points)
- $T$ = target values

