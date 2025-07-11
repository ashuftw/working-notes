---
title: Relationship between Fixed Point Iteration & Newton's Method
draft: false
tags: 
date: 2025-06-26
---
**Connection to Banach fixed-point iteration:** 
**For a Function**
- *Banach's Iteration* -> Finds fixed point.
- *Newton's Method* -> Finds zero. 

**Newton**'s method is an instance of the **Banach**'s iteration $x_{k+1} = g(x_{k})$ where $g(x) = x - \frac{f(x)}{f'(x)}$. 

Newton's method can be written as:

$$
g(x_{k+1})=x_{k+1} =x_k-\frac{f\left(x_k\right)}{f^{\prime}\left(x_k\right)}
$$


This is a fixed point iteration $x_{k+1}=g\left(x_k\right)$ where:

$$
g(x)=x-\frac{f(x)}{f^{\prime}(x)}
$$


Now, if $\mathrm{x}^*$ is a zero of $f$[^1] , then $\mathrm{f}\left(\mathrm{x}^*\right)=0$, which gives us:

$$
g\left(x^*\right)=x^*-\frac{f\left(x^*\right)}{f^{\prime}\left(x^*\right)}=x^*-\frac{0}{f^{\prime}\left(x^*\right)}=x^*
$$

So $\mathrm{x}^*$ is indeed a fixed point of $g$. The key insight is that zeros of $f$ correspond to fixed points of $g$.



[^1]: Because of this assumption, we don't apply the iteration formula, instead, use it as the condition that holds true. 
