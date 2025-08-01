---
title: Order of Consistency for Euler Method
draft: false
tags: 
date: 2025-07-24
---
### Euler Method
The Euler method is defined by $y_{i+1} = y_i + h f(t_i, y_i)$. The increment function is $\Phi(t,y,h) = f(t,y)$.

1.  **Truncation error :**

	$$
	\tau(t, h) = \frac{y(t+h) - y(t)}{h} - \Phi(t, y(t), h)
	$$

2.  **Use Taylor Series:**
    We expand $y(t+h)$ around $t$:

	$$
	y(t+h) = y(t) + h y'(t) + \mathcal{O}(h^2)
	$$
	Note: Comparing the expansion with the given rule, we get $y'= f$	
3.  **Substitute and Simplify:**

	$$
	\tau(t, h) = \frac{\left[y(t) + h y'(t) + \mathcal{O}(h^2)\right] - y(t)}{h} - f(t, y(t))
	$$


	$$
	\tau(t, h) = y'(t) + \mathcal{O}(h) - f(t, y(t))
	$$

    Since $y'(t) = f(t, y(t))$, the leading terms cancel:

	$$
	\tau(t, h) = \mathcal{O}(h)
	$$

The local truncation error is of the first order in $h$. Therefore, the Euler method has an **order of consistency of 1**.