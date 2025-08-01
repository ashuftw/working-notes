---
title: Order of Consistency for the Euler-Heun Method
draft: false
tags: 
date: 2025-07-24
---
#### Euler-Heun Method
$$
y(t+h) = y +  \frac{h}{2}\left[f(t, y) + f(\underline{t+h}, \underline{y + hf(t, y)})\right]
$$
The Euler-Heun method's increment function is $\Phi(t,y,h) = \frac{1}{2}[f(t,y) + f(t+h, y+hf(t,y))]$.

1.  **Set up the truncation error formula:**

	$$
	\tau(t, h) = \frac{y(t+h) - y(t)}{h} - \frac{1}{2}[f(t,y(t)) + f(t+h, y(t)+hf(t,y(t)))]
	$$

2.  **Use Taylor Series for all terms:**
    * **Left Part:** We expand $y(t+h)$ to a higher order: $y(t+h) = y(t) + hy'(t) + \frac{h^2}{2}y''(t) + \mathcal{O}(h^3)$. This gives:

    	$$
    	\frac{y(t+h)-y(t)}{h} = y'(t) + \frac{h}{2}y''(t) + \mathcal{O}(h^2)
    	$$

    * **Right Part:** We use a multivariate Taylor expansion for the second $f$ term:

    	$$
    	f(t+h, y+hf) = f(t,y) + h\frac{\partial f}{\partial t} + (hf)\frac{\partial f}{\partial y} + \mathcal{O}(h^2)
    	$$

        So the full increment function is:

    	$$
    	\Phi(t,y,h) = \frac{1}{2}[f + (f + h\frac{\partial f}{\partial t} + hf\frac{\partial f}{\partial y} + \mathcal{O}(h^2))] = f + \frac{h}{2}\left(\frac{\partial f}{\partial t} + f\frac{\partial f}{\partial y}\right) + \mathcal{O}(h^2)
    	$$

3.  **Substitute and Simplify:**
    Using $y' = f$ and $y'' = \frac{\partial f}{\partial t} + f\frac{\partial f}{\partial y}$, the increment function becomes:

	$$
	\Phi(t, y(t), h) = y'(t) + \frac{h}{2}y''(t) + \mathcal{O}(h^2)
	$$

    Now, we substitute everything back into the truncation error formula:

	$$
	\tau(t,h) = \left(y'(t) + \frac{h}{2}y''(t) + \mathcal{O}(h^2)\right) - \left(y'(t) + \frac{h}{2}y''(t) + \mathcal{O}(h^2)\right) = \mathcal{O}(h^2)
	$$

The local truncation error is of the second order in $h$. Therefore, the Euler-Heun method has an **order of consistency of 2**.