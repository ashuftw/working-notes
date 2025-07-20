---
title: Numerical Methods - Practice Test
draft: true
tags: 
date: 2025-06-23
---

## Task 1 
![[../Files/Pasted image 20250623173357.png]]
### Solution
![[../Files/IMG_20250623_184629360.jpg]]

Constant means the degree is $0$
## Task 2 
![[../Files/Pasted image 20250624104927.png]]
### Solution 
[[230507 Quadrature - Derivation and Formulae]]
**Quadrature error estimation**
- $f^{\prime \prime}(x)=12 c_1 x^2+6 c_2 x=-x^2+2 x$
- Check: $f^{\prime \prime}(-1)=-3, f^{\prime \prime}(1)=1, f^{\prime \prime}(3)=-3$
- Therefore $M_2=3$

**Error bound (in formulary)** 
$$
|R(f)| \leq \frac{(b-a)^3}{12} M_2
$$

$$
|R(f)| \leq \frac{(3-(-1))^3}{12} \cdot 3=\frac{64}{12} \cdot 3=16
$$

For $c_1=c_2=0, c_3, c_4 \in \mathbb{R}$ :
$f(x)=c_3 x+c_4$ is a polynomial of degree $1$ .

Since the trapezoid rule has degree of accuracy 1, it integrates all polynomials of degree $\leq 1$ exactly.

Therefore, the quadrature error is exactly 0 .


**Exam relevance**: Error estimation formulas are frequently tested!
## Task 3 
![[../Files/Pasted image 20250624123835.png]]
### Solution
#### Part (a) - Romberg Extrapolation for Forward Difference Quotient

The forward difference quotient has the form: 
$$
f'(x) \approx \frac{f(x+h) - f(x)}{h}
$$

From Taylor expansion: 
$$
f(x+h) = f(x) + hf'(x) + \frac{h^2}{2}f''(x) + O(h^3)
$$
Rearranging, we have 
$$
\frac{f(x+h) - f(x)}{h} = f'(x) + \overbrace{\frac{h}{2}f''(x) + O(h^2)}^{O(h)}
$$

This shows the forward difference quotient has **convergence order** **1**.
**Applying Romberg extrapolation**
Let $A(h) = \frac{f(x+h) - f(x)}{h}$ and $\frac{f^{\prime \prime}(x)}{2} = c$

Then we have 
$$
A(h) = f'(x) + ch + O(h^2)
$$
- $A(h) = f'(x) + ch + O(h^2)$
- $A(h/2) = f'(x) + c\frac{h}{2} + O(h^2)$

Using Romberg's formula with $q = 1$: 
$$
A_{new} = \frac{2A(h/2) - A(h)}{2-1} = 2A(h/2) - A(h)= f'(x)+O(h^2)
$$

 **Convergence order 2**.

Substituting to get the calculation formula: 

$$
Q_{new} = 2 \cdot \frac{f(x+h/2) - f(x)}{h/2} - \frac{f(x+h) - f(x)}{h}
$$
 

$$
= \frac{-3f(x) + 4f(x+h/2) - f(x+h)}{h}
$$
##### **Common Mistakes**
***Why do we consider the full Taylor Polynomial?***
Because is acts as the Blueprint for the error. Note that in Romberg extrapolation is  basically a clever trick to cancel out the errors.  
***Why expand up to $f''$ and not directly use the $O(h)$ notation?***
Same answer as above: We need the term so that we can cancel it out! 


#### Part (b) - Numerical Approximations

For $f(x) = x^{-1}$ at $x = 1$ with $h = 1/2$:
- $f(1) = 1$
- $f(3/2) = 2/3$
- $f(1/2) = 2$

**Exact derivative:** $f'(x) = -x^{-2}$, so $f'(1) = -1$

**Forward difference quotient:** 

$$
f'(1) \approx \frac{f(3/2) - f(1)}{1/2} = -\frac{2}{3}
$$


**Romberg scheme from (a):** 

$$
f'(1) \approx \frac{-3f(1) + 4f(5/4) - f(3/2)}{1/2} =-\frac{14}{15}
$$

**Central difference quotient:** 
$$
f'(1) \approx \frac{f(3/2) - f(1/2)}{2 \cdot 1/2}  = -\frac{4}{3}
$$

**Comparison with exact value $f'(1) = -1$:**
- Forward difference: $-2/3$ (error = $1/3$)
- Romberg scheme: $-14/15$ (error = $1/15$)
- Central difference: $-4/3$ (error = $1/3$)

The Romberg scheme provides the best approximation, as expected from its higher convergence order.
## Task 4 (Nonlinear Equations)
![[../Files/Pasted image 20250624133133.png]]
**Note: Newton's method formulas are available in the formulary.**
#### Part a) Derive Newton's method from Taylor expansion (1 point)

Taylor expansion of $f(x)$ around point $x_k$:

$$
f(x) = f(x_k) + f'(x_k)(x - x_k) + O((x - x_k)^2)
$$


$$
f(x) \approx f(x_k) + f^\prime(x_k)(x - x_k)
$$

To find the zero, we set this linear approximation equal to zero: 

$$
0 = f(x_k) + f^\prime(x_k)(x - x_k)
$$

Solving for $x$ gives us the next iterate: 

$$
x = x_k - \frac{f(x_k)}{f^\prime(x_k)}
$$


Therefore, **Newton's method** is: 

$$
\boxed{
x_{k+1} = x_k - \frac{f(x_k)}{f'(x_k)}}
$$

#### Part b) Calculate two Newton steps (2 points)
For $f(x) = \frac{1}{4}x^2$, we have $f'(x) =\frac{1}{2}x$
Starting from $x_0 = 4$:

$$
x_1 = x_0 - \frac{f(x_0)}{f'(x_0)} =  2
$$


$$
x_2 = x_1 - \frac{f(x_1)}{f'(x_1)} = 1
$$


**Explanation**: Newton's method approximates $f$ by its tangent line at each iteration and finds where the tangent intersects the $x-$axis.
![[../Files/Figure_1.png|center|600]]
Sketch should show parabola $f(x) = \frac{1}{4}x^2$, starting point $(4,4)$, tangent line at $x=4$ intersecting $x-$axis at $x=2$, then tangent at $x=2$ intersecting at $x=1$
#### Part c) Connection to Banach iteration and convergence order (2 points)

- [[250626 Relationship between Fixed Point Iteration & Newton's Method|Connection between Fixed Point Iteration & Newton's Method]]
- **Convergence order:** The derivative of the iteration function is:

$$
g'(x) = 1 - \frac{f'(x)^2 - f(x)f''(x)}{[f'(x)]^2} = \frac{f(x)f''(x)}{[f'(x)]^2}
$$


At the root $x*$ where $f(x*) = 0$: 

$$
g'(x*) = \frac{f(x*)f''(x*)}{[f'(x*)]^2} = 0
$$


Since $g'(x*) = 0$, Newton's method has **quadratic convergence (order 2)** near the root, assuming $f'(x*)\ne 0$ and $f''(x*)$ exists.

This means the error approximately squares in each iteration: $|x_{k+1} - x*| ≈ C|x_k - x*|^2$ for some constant $C$

