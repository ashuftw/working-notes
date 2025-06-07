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
