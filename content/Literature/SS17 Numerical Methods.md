---
title: SS17 Numerical Methods
draft: true
tags: 
date: 2025-05-21
---
## En
### Task 1 (5 points)
Using Lagrange interpolation, determine a polynomial $p$ through the points $(x_i, f(x_i))$, $i = 0, 1, 2$ for $f(x) = x^3$ and $x_0 = -1$, $x_1 = 0$, and $x_2 = 1$. Estimate the interpolation error in the interval $[-1, 1]$ using the smallest possible constant.

#### Solution
**Finding the Lagrange interpolation polynomial:**
For the function $f(x) = x^3$ with nodes $x_0 = -1$, $x_1 = 0$, $x_2 = 1$ :
- $y_0 = f(-1) = (-1)^3 = -1$
- $y_1 = f(0) = 0^3 = 0$
- $y_2 = f(1) = 1^3 = 1$

The [[230417 Lagrange interpolation|Lagrange basis polynomials]] are:

$L_0^2(x) = \frac{x-x_1}{x_0-x_1} \cdot \frac{x-x_2}{x_0-x_2}= \frac{(x-0)(x-1)}{(-1-0)(-1-1)} = \frac{x(x-1)}{2} = \frac{x^2-x}{2}$

$L_1^2(x) = \frac{(x+1)(x-1)}{(0+1)(0-1)} = \frac{x^2-1}{-1} = 1-x^2$

$L_2^2(x) = \frac{(x+1)(x-0)}{(1+1)(1-0)} = \frac{x(x+1)}{2} = \frac{x^2+x}{2}$

The interpolation polynomial is: 
$$
p(x) = y_0 L_0^2(x) + y_1 L_1^2(x) + y_2 L_2^2(x)
$$
 
$$
p(x) = (-1) \cdot \frac{x^2-x}{2} + 0 \cdot (1-x^2) + 1 \cdot \frac{x^2+x}{2}
$$
 
$$
p(x) = \frac{-(x^2-x) + (x^2+x)}{2} = \frac{2x}{2} = x
$$


**Estimating the interpolation error:**

_Note: The interpolation error formula is available in the formulary._

For $f \in C^{N+1}([a,b])$ with $N+1$ interpolation points, the error is: 
$$
|f(x) - p_N(x)| = \frac{|\omega(x)|}{(N+1)!} |f^{(N+1)}(\xi)|
$$


where $\omega(x) = \prod_{i=0}^N (x-x_i)$ and $\xi \in [a,b]$.

For our case:

- $N = 2$ (degree 2 polynomial)
- $f(x) = x^3$, so $f^{(3)}(x) = 6$ (constant)
- $\omega(x) = (x+1)(x-0)(x-1) = x(x^2-1) = x^3-x$

The error estimate becomes: 
$$
|r(x)| = \frac{|x^3-x|}{3!} \cdot 6 = |x^3-x|
$$

**Find Maximum Error**
![[../Files/Pasted image 20250613123920.png|center|400]]
To find the maximum, we first find critical points (location in the domain where slope is zero because that's where the candidates for max error lie)

**Critical points**
Setting $r'(x) = 0$

$$
3x^2 - 1 = 0 \implies x^2 = \frac{1}{3} \implies x = \pm \frac{1}{\sqrt{3}}
$$


**Given bounds** $x \in [-1,1]$

**Evaluate errors at critical points and bounds**
* $|r(-1)| = |(-1)^3 - (-1)| = |-1 + 1| = 0$
* $|r(1)| = |(1)^3 - 1| = |1 - 1| = 0$
* $|r(-\frac{1}{\sqrt{3}})| = |(-\frac{1}{\sqrt{3}})^3 - (-\frac{1}{\sqrt{3}})| = |-\frac{1}{3\sqrt{3}} + \frac{1}{\sqrt{3}}| = |\frac{2}{3\sqrt{3}}|$
* $|r(\frac{1}{\sqrt{3}})| = |(\frac{1}{\sqrt{3}})^3 - (\frac{1}{\sqrt{3}})| = |\frac{1}{3\sqrt{3}} - \frac{1}{\sqrt{3}}| = |-\frac{2}{3\sqrt{3}}|$

**Answer:**
- Interpolation polynomial: $p(x) = x$
- Maximum interpolation error: $\frac{2\sqrt{3}}{9} \approx 0.385$

### Task 2 (5 points)

Using Kepler's barrel rule, determine an approximation of $\int_0^{\pi} \sin x \, dx$ and estimate the quadrature error. Explain why the estimate approximates the actual error quite closely.
I'll solve this step-by-step using Kepler's barrel rule (Simpson's rule).
#### Solution
**Step 1: Apply [[230507 Quadrature - Derivation and Formulae|Kepler's barrel rule]]**
From the [[230507 Quadrature - Derivation and Formulae|formula]]: 

$$
\int_0^{\pi} \sin x , dx \approx \frac{\pi}{6}[0 + 4(1) + 0] = \frac{4\pi}{6} = \frac{2\pi}{3}
$$

**Step 2: Estimate the quadrature error**
From formulary, the error estimate is: 
$$
|R(f)| \leq \frac{(b-a)^5}{2880}M_4
$$

where $M_4 = \max_{x \in [0,\pi]} |f^{(4)}(x)|$.
- $f^{(4)}(x) = \sin x$
- $M_4 = \max_{x \in [0,\pi]} |\sin x| = 1$

Therefore: 

$$
|R(f)| \leq \frac{\pi^5}{2880} \approx \frac{306.02}{2880} \approx 0.1063
$$

**Step 3: Compare with actual error**

The exact value: $\int_0^{\pi} \sin x , dx = [-\cos x]_0^{\pi} = 2$

Actual error: $|2 - \frac{2\pi}{3}| = |2 - 2.0944| \approx 0.0944$

**Why the estimate is quite close:**
1. The function $\sin x$ is smooth and well-behaved on $[0,\pi]$
2. The maximum value $M_4 = 1$ occurs at $x = \pi/2$, which is near the middle of the interval where the error formula tends to be most accurate
3. Simpson's rule has degree of accuracy 3


### Task 3 (5 points)

Explain the idea of ​​Romberg extrapolation. State the Romberg scheme (at least two improvement levels), including the achieved orders of convergence, for numerical integration, starting with the summed trapezoidal rule.
#### Solution 
[[240603 Romberg's Extrapolation Method|Theoretical answer]]
**Romberg scheme for numerical integration starting with summed trapezoidal rule:**

The summed trapezoidal rule has the error expansion: 

$$
I(f) = Q_J(f) + Ch^2 + C_1h^4 + C_2h^6 + \ldots
$$


where $h$ is the step size and $Q_J(f)$ is the approximation with $J$ subintervals.

**The Romberg scheme:**
Starting values (summed trapezoidal rule):
- $Q^{(1)}_J(f)$ with step size $h$
- $Q^{(1)}_{2J}(f)$ with step size $h/2$
- $Q^{(1)}_{4J}(f)$ with step size $h/4$
- etc.

**First improvement level:**
$q = 2$ -> Trapezoidal Rule

$$
Q^{(2)}_J(f) = \frac{4Q^{(1)}_{2J}(f) - Q^{(1)}_J(f)}{3}
$$
 This eliminates the $h^2$ term from the error expansion, giving convergence order 4 (this is Simpson's rule).

**Note:** You could rewrite the expansion term and find the significant error term or we can just use the knowledge that each level improves the accuracy by one term in the expansion. 

**Second improvement level:**
$q$ is now 4! 

$$
Q^{(3)}_J(f) = \frac{16Q^{(2)}_{2J}(f) - Q^{(2)}_J(f)}{15}
$$
 This eliminates the $h^4$ term, giving convergence order 6.


**Convergence orders:**

- Level 1 (trapezoidal): Order 2
- Level 2 (Simpson): Order 4

**Schematic representation:**

```
Q^(1)_J     
         ↘
Q^(1)_2J    →  Q^(2)_J
         ↘            ↘
Q^(1)_4J    →  Q^(2)_2J  →  Q^(3)_J
         ↘            ↘            ↘
Q^(1)_8J    →  Q^(2)_4J  →  Q^(3)_2J  →  Q^(4)_J
```

**Quick remarks for exam:**

- This question has high relevance as Romberg extrapolation appears frequently in exams
- The general extrapolation formula is available in the formulary: $Q_{new} = \frac{2^q Q_{old,2J} - Q_{old,J}}{2^q - 1}$
### Task 4 (5 points)

Determine the Newton iteration for calculating a root of $f(x) = (x^2 - 2)^2$. Make reasoned statements about its order of convergence. Is it well suited for calculating $x_N = \sqrt{2}$?
#### Solution 
**Newton Iteration**
The Newton iteration is given by $x_{n+1}=x_n-\frac{f\left(x_n\right)}{f^{\prime}\left(x_n\right)}$.

$$
x_{n+1}=\frac{4 x_n^2-\left(x_n^2-2\right)}{4 x_n}=\frac{3 x_n^2+2}{4 x_n}
$$

**Order of Convergence**
The order of convergence is linear (order 1).
- Reasoning: Quadratic convergence requires the root $x^*$ to be a simple root, meaning $f^{\prime}\left(x^*\right) \neq 0$.
- The root of $f(x)$ is $x^*=\sqrt{2}$.
- Evaluating the derivative at the root:

$$
f^{\prime}(\sqrt{2})=4 \sqrt{2}\left((\sqrt{2})^2-2\right)=4 \sqrt{2}(2-2)=0 .
$$

- Since the derivative is zero at the root, the root has a [[250708 Multiplicity|Multiplicity]] greater than $1$, and the convergence degrades from quadratic to linear.


### Task 5 (5 points)
Derive the Euler-Heun method for the numerical solution of $y' = f(t, y)$, starting with the integral of $f(t, y)$ over $[t_i, t_{i+1}]$. Indicate exact and approximate values, as well as the approximations used. State properties of the Euler-Heun method.
#### Solution
[[250709 Euler-Heun Method|Derivation]]
### Task 6 (5 points)

Prove that the implicit midpoint rule $y_{i+1} = y_i + h f \left(t_i + \frac{h}{2}, \frac{1}{2}(y_i + y_{i+1})\right)$ has at least order of consistency $2$.

#### Solution
To prove consistency order 2, we need to show that the local truncation error $\tau(t,h) = O(h^2)$.

**Given:** $y_{i+1} = y_i + h f\left(t_i + \frac{h}{2}, \frac{y_i + y_{i+1}}{2}\right)$

**Proof:**

From Formulary, the local truncation error is: 

$$
\begin{aligned}
\tau=&\frac{y(t+h)-y(t)}{h}-\Phi(t, y(t), h)\\ \\
\ = &\frac{y(t+h) - y(t)}{h} - f\left(t + \frac{h}{2}, \frac{y(t) + y(t+h)}{2}\right)
\end{aligned}
$$

> **Note:** Locally, we substitute $y(t_i) =  y(t)$ and $y\left(t_{i+1}\right)=y(t+h)$

**Step 1:** Taylor expand $y(t+h)$ around $t$: 
$$
y(t+h) = y(t) + hy'(t) + \frac{h^2}{2}y''(t) + O(h^3)
$$


**Step 2:** Comparing the Taylor expansion with the given rule, we get  $y'(t) = f(t,y(t))$. Hence we need to expand $f\left(t + \frac{h}{2}, \frac{y(t) + y(t+h)}{2}\right)$.

First, find $\frac{y(t) + y(t+h)}{2}$: 

$$
\begin{aligned}
\frac{y(t) + y(t+h)}{2} = & \frac{y(t)+\overbrace{\left(y(t)+h y^{\prime}(t)+\frac{h^2}{2} y^{\prime \prime}(t)+O\left(h^3\right)\right)}^{\text{from Taylor Expansion}}}{2}
 \\

= &y(t) + \frac{h}{2}y'(t) + \frac{h^2}{4}y''(t) + O(h^3)
\end{aligned}
$$


**Step 3:** Multivariable Taylor expansion of $f$ around $(t, y(t))$: 

$$
f(a+\Delta x, b+\Delta z) \approx f(a, b)+\Delta x \cdot \frac{\partial f}{\partial x}+\Delta z \cdot \frac{\partial f}{\partial z}+\text { Higher-Order Terms }
$$

In our case

$$
f\left(t + \frac{h}{2}, \frac{y(t) + y(t+h)}{2}\right) = f(t,y(t)) + \frac{h}{2}f_t + \left(\frac{h}{2}y'(t) + O(h^2)\right)f_y + O(h^2)
$$


Since $y'(t) = f(t,y(t))$: 
$$
= f(t,y(t)) + \frac{h}{2}f_t + \frac{h}{2}f(t,y(t))f_y + O(h^2)
$$


**Step 4:** Note that $y''(t) = \frac{d}{dt}f(t,y(t)) = f_t + f_y y'(t) = f_t + f_y f$

Therefore **Step 3** becomes: 

$$
\begin{aligned}
f\left(t + \frac{h}{2}, \frac{y(t) + y(t+h)}{2}\right) =&  \underbrace{f(t, y(t))}_{y^{\prime}(t)}+\underbrace{\frac{h}{2}\left(f_t+y^{\prime}(t) f_y\right)}_{\frac{h}{2} y^{\prime \prime}(t)}+O\left(h^2\right)
\\
 = & y'(t) + \frac{h}{2}y''(t) + O(h^2)
\end{aligned}
$$


**Step 5:** Substitute into the truncation error: 
$$
\tau(t,h) = \frac{y(t) + hy'(t) + \frac{h^2}{2}y''(t) + O(h^3) - y(t)}{h} - \left(y'(t) + \frac{h}{2}y''(t) + O(h^2)\right)
$$



$$
= y'(t) + \frac{h}{2}y''(t) + O(h^2) - y'(t) - \frac{h}{2}y''(t) - O(h^2)
$$



$$
= O(h^2)
$$


**Conclusion:** The implicit midpoint rule has consistency order at least 2. ✓

---

**Exam relevance:** This is a standard proof technique for consistency order. The key steps are:

1. Taylor expand the exact solution
2. Taylor expand the method's right-hand side
3. Use the chain rule for derivatives: $y''(t) = f_t + f_y f$
4. Show cancellation up to order $h^2$

**Formula sheet note:** The definition of truncation error and consistency order should be in your formulary.




### Task 7 (5 points)

Write down the procedure for the Butcher scheme:


$$
\begin{array}{c|cc}
& 1/3 & 5/12 & -1/12 \\
& 1 & 3/4 & 1/4 \\
\hline
& & 3/4 & 1/4
\end{array}
$$


Using the calculation rule, explain whether the resulting procedure is explicit or implicit.
#### Solution 
**[[250709 Runge-Kutta Method Procedure|Runge-Kutta Method Procedure]]**
For a 2-stage Runge-Kutta method with the given tableau


$$
k_1 = hf\left(t_i + \frac{1}{3}h, y_i + \frac{5}{12}hk_1 - \frac{1}{12}hk_2\right)
$$



$$
\boxed{
k_2 = hf\left(t_i + h, y_i + \frac{3}{4}hk_1 + \frac{1}{4}hk_2\right)
}
$$




$$
y_{i+1} = y_i + \frac{3}{4}k_1 + \frac{1}{4}k_2
$$

The Procedure is **Implicit**
1. In the first equation, $k_1$ depends on itself (coefficient $\frac{5}{12} \neq 0$ ) and on $k_2$
2. In the second equation, $k_2$ depends on itself (coefficient $\frac{1}{4} \neq 0$ )

### Task 8 (5 points)
Apply the line method to the one-dimensional wave equation $u_{tt} = c^2 u_{xx}$ with homogeneous Dirichlet boundary conditions at $x = 0$ and $x = 1$, and write down the resulting system of ordinary differential equations. What is the corresponding system in matrix notation? What does the CFL condition say for this problem?
### Solution
Given: $u_{t t}=c^2 u_{x x}$ with $u(t, 0)=u(t, 1)=0$

**Spatial Discretization**
Using grid points $x_j=j \Delta x$ where $\Delta x=\frac{1}{n}, j=0,1, \ldots, n$
Approximate $u_{x x}$ at interior points using central differences:

$$
u_{x x}\left(t, x_j\right) \approx \frac{u_{j-1}(t)-2 u_j(t)+u_{j+1}(t)}{\Delta x^2}
$$

where $u_j(t) \approx u\left(t, x_j\right)$

**Substituting in the given PDE**
For $j=1,2, \ldots, n-1$ :

$$
u_j^{\prime \prime}(t)=\frac{c^2}{\Delta x^2}\left[u_{j-1}(t)-2 u_j(t)+u_{j+1}(t)\right]
$$


With boundary conditions: $u_0(t)=u_n(t)=0$
**Writing the system in Matrix form**

$$
u^{\prime \prime}(t)=\frac{c^2}{\Delta x^2}\left[\begin{array}{ccccc}
-2 & 1 & 0 & \cdots & 0 \\
1 & -2 & 1 & \cdots & 0 \\
0 & \ddots & \ddots & \ddots & 0 \\
\vdots & & 1 & -2 & 1 \\
0 & \cdots & 0 & 1 & -2
\end{array}\right]\left[\begin{array}{c}
u_1(t) \\
u_2(t) \\
\vdots \\
u_{n-1}(t)
\end{array}\right]
$$

**In vector notation**

$$
\mathbf{u}^{\prime \prime}(t)=\frac{c^2}{\Delta x^2} A \mathbf{u}(t)
$$




**Conversion to First-Order System**
Introduce $v_j(t)=u_j^{\prime}(t)$ to get:
Let $\mathbf{u}=\left[u_1, \ldots, u_{n-1}\right]^T$ and $\mathbf{v}=\left[v_1, \ldots, v_{n-1}\right]^T$

$$
\left[\begin{array}{c}
\mathbf{u}^{\prime} \\
\mathbf{v}^{\prime}
\end{array}\right]=\left[\begin{array}{cc}
0 & I \\
\frac{c^2}{\Delta x^2} A & 0
\end{array}\right]\left[\begin{array}{l}
\mathbf{u} \\
\mathbf{v}
\end{array}\right]
$$

**CFL Condition**
For explicit time integration methods, stability requires:

$$
\Delta t \leq \frac{\Delta x}{c}
$$


This ensures that the numerical domain of dependence contains the physical domain of dependence. The information propagation speed $c$ limits the time step relative to the spatial discretization.

### Task 9 (Additional, 3 points)
Explain the concept of $A$-stability of numerical methods for solving ordinary differential equations. Formulate statements about the $A$-stability of explicit and implicit one-step methods. What special property does the Crank-Nicolson method have?

## DE

### Aufgabe 1 (5 Punkte)

Bestimmen Sie mit der Lagrange-Interpolation ein Polynom $p$ durch die Punkte $(x_i, f(x_i))$, $i = 0, 1, 2$ für $f(x) = x^3$ und $x_0 = -1$, $x_1 = 0$ und $x_2 = 1$. Schätzen Sie den 
Interpolationsfehler im Intervall $[-1, 1]$ durch eine möglichst kleine Konstante ab. 

### Aufgabe 2 (5 Punkte)

Bestimmen Sie mit der Keplerschen Fassregel eine Näherung von $\int_0^{\pi} \sin x \, dx$, und schätzen Sie den Quadraturfehler ab. Begründen Sie, warum die Abschätzung den tatsächlichen Fehler recht genau trifft.

### Aufgabe 3 (5 Punkte)

Erläutern Sie die Idee der Romberg-Extrapolation. Geben Sie das Romberg-Schema (mindestens zwei Verbesserungsstufen) inklusive der erreichten Konvergenzordnungen für die numerische Integration beginnend mit der summierten Trapezregel an.

### Aufgabe 4 (5 Punkte)

Bestimmen Sie die Newton-Iteration zur Berechnung einer Nullstelle von $f(x) = (x^2 - 2)^2$. Machen Sie begründet Aussagen über ihre Konvergenzordnung. Ist sie zur Berechnung von $x_N = \sqrt{2}$ gut geeignet?

### Aufgabe 5 (5 Punkte)

Leiten Sie das Euler-Heun-Verfahren zur numerischen Lösung von $y' = f(t, y)$ her, und beginnen Sie bei dem Integral von $f(t, y)$ über $[t_i, t_{i+1}]$. Kennzeichnen Sie exakte Werte und Näherungswerte sowie die verwendeten Näherungen. Nennen Sie Eigenschaften des Euler-Heun-Verfahrens.

### Aufgabe 6 (5 Punkte)

Beweisen Sie, dass die implizite Mittelpunktsregel $y_{i+1} = y_i + h f \left(t_i + \frac{h}{2}, \frac{1}{2}(y_i + y_{i+1})\right)$ mindestens die Konsistenzordnung 2 hat.

### Aufgabe 7 (5 Punkte)

Notieren Sie das Verfahren zum Butcher-Schema 


$$
\begin{array}{c|cc}
 & 1/3 & 5/12 & -1/12 \\
 & 1 & 3/4 & 1/4 \\
\hline
 & & 3/4 & 1/4
\end{array}
$$


Begründen Sie anhand der Rechenvorschrift, ob das entstehende Verfahren explizit oder implizit ist.

### Aufgabe 8 (5 Punkte)
Wenden Sie die Linienmethode auf die eindimensionale Wellengleichung $u_{tt} = c^2 u_{xx}$ mit homogenen Dirichlet-Randbedingungen bei $x = 0$ und $x = 1$ an, und notieren Sie das entstehende System von gewöhnlichen Differentialgleichungen. Wie lautet das zugehörige System in Matrixschreibweise? Was besagt die CFL-Bedingung für dieses Problem?

### Aufgabe 9 (Zusatz, 3 Punkte)
Erläutern Sie das Konzept der $A$-Stabilität von numerischen Verfahren zur Lösung von gewöhnlichen Differentialgleichungen. Formulieren Sie Aussagen über die $A$-Stabilität von expliziten und impliziten Einschrittverfahren. Welche besondere Eigenschaft hat das Crank-Nicolson-Verfahren?