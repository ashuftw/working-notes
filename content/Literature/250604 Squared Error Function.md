---
title: Squared Error Function
draft: false
tags: 
date: 2025-06-04
---


$$
E(w)=\frac{1}{2} \sum_{n=1}^N\left(y\left(x_n, w\right)-t_n\right)^2
$$


Remember:
- $1/2$ factor (makes derivative cleaner)
- Sum over all $N$ data points
- Squared difference between:
	- $y\left(x_n, w\right)=$ model prediction
	- $t_n=$ target/actual value

> *Mnemonic: "Half the Sum of Squared differences"*
> *Note: Sometimes written as $\frac{1}{2 N}$ for averaging*

## Generalized Squared Error 

$$
\tilde{E}(\mathbf{w}) = \frac{1}{2}\sum_n (t_n - \mathbf w^T\phi(x_n))^2 +\frac{\lambda}{2}||\mathbf w||^2
$$

- $\mathbf w$ is the **parameter vector** (weights) that the model learns (and optimized during training).
- $\phi(x)$ is the [[250620 Basis Functions|Basis Function vector]] which Transforms the raw input x into a higher-dimensional feature space
- Transforms the raw input $x$ into a higher-dimensional feature space
-  The dot product $w^T \phi(x)$ gives the model's prediction