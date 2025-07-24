---
title: Quadrature - Derivation and Formulae
draft: false
date: 2023-05-07
---
It is a Numerical tool that is used to find the area under a curve without performing a symbolic integration. Some of the basic Quadratures are as follows. 

### 1. Left rectangle rule	



$$
Q(f)=f(a)(b-a)
$$



### 2. Right rectangle rule 



$$
Q(f)=f(b)(b-a)
$$



### 3. Midpoint rule



$$
Q(f)= f\left(\frac{a+b}{2}\right)(b-a)
$$



### 4. Trapezoid rule 



$$
Q(f)=\frac{f(a)+f(b)}{2}\left(b-a\right)
$$



### 5. Kepler / Simpson's Rule 



$$
Q(f)= \frac{b-a}{6}\left[f(a)+4 f\left(\frac{a+b}{2}\right)+f(b)\right]
$$



## Derivations
### Left/Right Rectangle Rule 
**Idea:** Approximate $f$ by constant polynomial $f(a)$ on $[a,b]$ 


$$
p_0(x) = f(a)
$$




$$
\boxed{\int_a^b f(x)dx \approx (b-a)f(a)}
$$


And by constant $f(b)$ for Right Rectangle Rule 
### Midpoint Rule 
**Step 1:** interpolate $f$ at midpoint $m = \frac{a+b}{2}$ with constant polynomial: 


$$
p_0(x) = f(m)
$$




**Step 2:** Integrate the constant: 

$$
I(f) \approx \int_a^b f(m)dx = f(m) \cdot (b-a)
$$



**Result:** 

$$
\boxed{\int_a^b f(x)dx \approx (b-a)f\left(\frac{a+b}{2}\right)}
$$




### Trapezoid Rule 
Interpolate $f$ using Lagrange basis polynomials at points $(a, f(a) )$ and $(b, f(b) )$:


$$
p_1(x)=f(a) \cdot L_0(x)+f(b) \cdot L_1(x)
$$


where:
- $L_0(x)=\frac{x-b}{a-b}$ (equals $1$ at $\mathrm{x}=\mathrm{a}, 0$ at $\mathrm{x}=\mathrm{b}$ )
- $L_1(x)=\frac{x-a}{b-a}$ (equals $0$ at $\mathrm{x}=\mathrm{a}, 1$ at $\mathrm{x}=\mathrm{b}$ )
So,


$$
p_1(x)=f(a) \frac{x-b}{a-b}+f(b) \frac{x-a}{b-a}
$$




$$
I(f) \approx \int_a^b p_1(x) d x
$$


It can be calculated
- $\int_a^b \frac{x-b}{a-b} d x=\frac{b-a}{2}$
- $\int_a^b \frac{x-a}{b-a} d x=\frac{b-a}{2}$



	$$
	\boxed{
	I(f) \approx \frac{b-a}{2}[f(a)+f(b)]
	}
	$$



### Simpson's/Kepler's Rule

**Step 1:** Interpolate f through three points: $(a,f(a))$, $(m,f(m))$, $(b,f(b))$ where $m = \frac{a+b}{2}$

**Step 2:** The quadratic polynomial is: 

$$
p_2(x) = f(a)L_0(x) + f(m)L_1(x) + f(b)L_2(x)
$$


**Step 3:** Key insight - for equidistant points:

- $\int_a^b L_0(x)dx = \frac{b-a}{6}$
- $\int_a^b L_1(x)dx = \frac{4(b-a)}{6}$
- $\int_a^b L_2(x)dx = \frac{b-a}{6}$

**Result:** 


$$
\boxed{\int_a^b f(x)dx \approx \frac{b-a}{6}[f(a) + 4f(m) + f(b)]}
$$



