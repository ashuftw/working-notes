---
title:  The Taylor Expansion
draft: false
date: 2023-11-15
---

![[Pasted image 20231115125339.png|center|300]]
## Taylor Series

$$
f(x) = f(a) + f'(a)(x - a) + \frac{f''(a)}{2!}(x - a)^2 + \ldots
$$


$$
\boxed{f(x) = \sum_{n=0}^{\infty} \frac{f^{(n)}(a)}{n!}(x - a)^n }
$$

where,
- $x\rightarrow$ domain
- $a\in x\rightarrow$ center of the series i.e. the point around which the Taylor approximation holds.

## Maclaurin Series $a=0$ 
Point of approximation is the origin

$$
\boxed{f(x) = \sum_{n=0}^{\infty} \frac{f^{(n)}(0)}{n!}x^n}
$$


## Taylor Expansion of $f(x+h)$
Function to be evaluated at $(x+h)$. 
Center of the series $a = x$

$$
\begin{align*}
f(x+h) &= f(x) + f'(x)((x+h) - x) + \frac{f''(x)}{2!}((x+h) - x)^2 + \ldots
\\
f(x+h) &= f(x) + f'(x)\cdot h + \frac{f''(x)}{2!}\cdot h^2 + \ldots
\end{align*}
$$


$$
\boxed{
f(x+h) = \sum_{n=0}^\infty \frac{f^{(n)}(x)}{n !} \cdot h^n
}
$$



