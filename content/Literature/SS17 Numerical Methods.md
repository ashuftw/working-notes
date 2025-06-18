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

The interpolation polynomial is: $$p(x) = y_0 L_0^2(x) + y_1 L_1^2(x) + y_2 L_2^2(x)$$ $$p(x) = (-1) \cdot \frac{x^2-x}{2} + 0 \cdot (1-x^2) + 1 \cdot \frac{x^2+x}{2}$$ $$p(x) = \frac{-(x^2-x) + (x^2+x)}{2} = \frac{2x}{2} = x$$

**Estimating the interpolation error:**

_Note: The interpolation error formula is available in the formulary._

For $f \in C^{N+1}([a,b])$ with $N+1$ interpolation points, the error is: $$|f(x) - p_N(x)| = \frac{|\omega(x)|}{(N+1)!} |f^{(N+1)}(\xi)|$$

where $\omega(x) = \prod_{i=0}^N (x-x_i)$ and $\xi \in [a,b]$.

For our case:

- $N = 2$ (degree 2 polynomial)
- $f(x) = x^3$, so $f^{(3)}(x) = 6$ (constant)
- $\omega(x) = (x+1)(x-0)(x-1) = x(x^2-1) = x^3-x$

The error estimate becomes: $$|r(x)| = \frac{|x^3-x|}{3!} \cdot 6 = |x^3-x|$$
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
**Step 1: Apply [[230507 Quadrature|Kepler's barrel rule]]**
From the [[230507 Quadrature|formula]]: 
$$
\int_0^{\pi} \sin x , dx \approx \frac{\pi}{6}[0 + 4(1) + 0] = \frac{4\pi}{6} = \frac{2\pi}{3}
$$
**Step 2: Estimate the quadrature error**
From formulary, the error estimate is: $$|R(f)| \leq \frac{(b-a)^5}{2880}M_4$$
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

### Task 4 (5 points)

Determine the Newton iteration for calculating a root of $f(x) = (x^2 - 2)^2$. Make reasoned statements about its order of convergence. Is it well suited for calculating $x_N = \sqrt{2}$?

### Task 5 (5 points)

Derive the Euler-Heun method for the numerical solution of $y' = f(t, y)$, starting with the integral of $f(t, y)$ over $[t_i, t_{i+1}]$. Indicate exact and approximate values, as well as the approximations used. State properties of the Euler-Heun method.

### Task 6 (5 points)

Prove that the implicit midpoint rule $y_{i+1} = y_i + h f \left(t_i + \frac{h}{2}, \frac{1}{2}(y_i + y_{i+1})\right)$ has at least order of consistency 2.

### Task 7 (5 points)

Write down the procedure for the Butcher scheme:

$$\begin{array}{c|cc}
& 1/3 & 5/12 & -1/12 \\
& 1 & 3/4 & 1/4 \\
\hline
& & 3/4 & 1/4
\end{array}$$

Using the calculation rule, explain whether the resulting procedure is explicit or implicit.

### Task 8 (5 points)
Apply the line method to the one-dimensional wave equation $u_{tt} = c^2 u_{xx}$ with homogeneous Dirichlet boundary conditions at $x = 0$ and $x = 1$, and write down the resulting system of ordinary differential equations. What is the corresponding system in matrix notation? What does the CFL condition say for this problem?

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

$$\begin{array}{c|cc}
 & 1/3 & 5/12 & -1/12 \\
 & 1 & 3/4 & 1/4 \\
\hline
 & & 3/4 & 1/4
\end{array}$$

Begründen Sie anhand der Rechenvorschrift, ob das entstehende Verfahren explizit oder implizit ist.

### Aufgabe 8 (5 Punkte)
Wenden Sie die Linienmethode auf die eindimensionale Wellengleichung $u_{tt} = c^2 u_{xx}$ mit homogenen Dirichlet-Randbedingungen bei $x = 0$ und $x = 1$ an, und notieren Sie das entstehende System von gewöhnlichen Differentialgleichungen. Wie lautet das zugehörige System in Matrixschreibweise? Was besagt die CFL-Bedingung für dieses Problem?

### Aufgabe 9 (Zusatz, 3 Punkte)
Erläutern Sie das Konzept der $A$-Stabilität von numerischen Verfahren zur Lösung von gewöhnlichen Differentialgleichungen. Formulieren Sie Aussagen über die $A$-Stabilität von expliziten und impliziten Einschrittverfahren. Welche besondere Eigenschaft hat das Crank-Nicolson-Verfahren?