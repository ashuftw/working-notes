---
title: Order of Consistency of the Implicit Midpoint Rule
draft: false
tags: 
date: 2025-07-23
---

**Note:** This is a standard proof technique for consistency order. The key steps are:

1. Taylor expand the exact solution
2. Taylor expand the method's right-hand side
3. Use the chain rule for derivatives: $y''(t) = f_t + f_y f$
4. Show cancellation up to order $h^2$
--- 
**The Implicit Midpoint rule** 

$$
y_{i+1} = y_i + h f \left(t_i + \frac{h}{2}, \frac{1}{2}(y_i + y_{i+1})\right)
$$

**The increment function** 

$$
\Phi(t,y,h) = f\left(t + \frac{h}{2}, \frac{1}{2}(y(t) + y(t+h))\right)
$$

#### 1.  **Local Truncation Error**
From Formulary
$$
\tau(t, h) = \frac{y(t+h) - y(t)}{h} - \Phi(t, y(t), h)
$$
$$
\tau(t, h) = \frac{y(t+h) - y(t)}{h} - f\left(t + \frac{h}{2}, \frac{1}{2}(y(t) + y(t+h))\right)
$$

#### 2.  **Taylor Series Expansions**
   We use Taylor series to expand the terms around the point $(t, y(t))$.
   **First Term:** Expanding $y(t+h)$ around $t$ yields:
$$
y(t+h) = y(t) + h y'(t) + \frac{h^2}{2} y''(t) + \mathcal{O}(h^3)
$$
> Note: Comparing the expansion with the given rule, we get $y'= f$	
Rearranging,        
$$
\frac{y(t+h) - y(t)}{h} = y'(t) + \frac{h}{2} y''(t) + \mathcal{O}(h^2)
$$
**Second Term:** We first expand the spatial argument of $f$: 
$$
\begin{align} \frac{1}{2}(y(t) + y(t+h)) &= \frac{1}{2}(y(t) + \overbrace{[y(t) + h y'(t) + \mathcal{O}(h^2)]}^\text{Taylor expansion})\\ &= y(t) + \frac{h}{2}y'(t) + \mathcal{O}(h^2)\end{align}
$$
Now we perform a multivariate Taylor expansion of $f$ around $(t, y(t))$:
$$
f(a+\Delta x, b+\Delta y) \approx f(a, b)+\Delta x \cdot \frac{\partial f}{\partial x}+\Delta y \cdot \frac{\partial f}{\partial y}+\text { Higher-Order Terms }
$$
We have  
$$
f\left(t + \overbrace{\frac{h}{2}}^{\Delta x}, y(t) + \overbrace{\frac{h}{2}y'(t) + \mathcal{O}(h^2)}^{\Delta y}\right) = f(t, y(t)) + \frac{h}{2} \frac{\partial f}{\partial t} + \frac{h}{2}y'(t) \frac{\partial f}{\partial y} + \mathcal{O}(h^2)
$$
Since $y'(t) = f(t, y(t))$ and, by the chain rule, $y''(t) = \frac{d}{dt}f(t, y(t)) = \frac{\partial f}{\partial t} + \frac{\partial f}{\partial y} y'(t)$, the expansion simplifies to:
$$
f\left(\dots\right) = f(t, y(t)) + \frac{h}{2} y''(t) + \mathcal{O}(h^2) = y'(t) + \frac{h}{2} y''(t) + \mathcal{O}(h^2)
$$
#### 3.  **Combine the Expansions**
Substituting the expanded forms back into the truncation error formula, we get:
$$
\tau(t, h) = \left[y'(t) + \frac{h}{2} y''(t) + \mathcal{O}(h^2)\right] - \left[y'(t) + \frac{h}{2} y''(t) + \mathcal{O}(h^2)\right]
$$
$$
\boxed{\tau(t, h) = \mathcal{O}(h^2)}
$$

Since the local truncation error is of the order $\mathcal{O}(h^2)$, the implicit midpoint rule has an **order of consistency of at least 2**.
