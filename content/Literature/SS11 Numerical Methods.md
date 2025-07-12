---
title: SS11 Numerical Methods
draft: true
tags: 
date: 2025-05-21
---
## Engineering Mathematics VI Exam

**Completion time:** 90 minutes
**Resources:** A written A4 sheet of paper, calculator

### Task 1 (5 points)

Using Lagrange interpolation, determine an interpolation polynomial through the points $(1, 1)^T$, $(2, 0)^T$, and $(3, -3)^T$.

### Task 2 (5 points)

Using Kepler's barrel rule, determine an approximation of $\int_0^{\pi} \sin \frac{x}{2} dx$ and estimate the quadrature error.

### Task 3 (5 points)

Approximate the integral $\int_0^1 x^2 dx$ using the summed trapezoidal rule for $J = 1$, $J = 2$, and $J = 4$ for equidistant nodes, and perform two steps of the Romberg extrapolation.

### Task 4 (5 points)

Using the second-order central difference quotient with $h = 0.1$, determine an approximation for the second derivative of $f(x) = x^2$ at the point $x_0 = 1$. Why do you obtain an error-free value?

### Task 5 (5 points)

Perform two steps of Newton's method to determine a zero of $f(x) = x^2$ with the starting value $x_0 = 1$. What order of convergence do you observe? What general statements can be made about the order of convergence of Newton's method?

### Task 6 (5 points)

Perform one step of the Euler-Heun method to solve the initial value problem $y' = t - ty$, $y(0) = 2$ with a step size of $h = 0.2$.

### Task 7 (5 points)

Apply one step of the Crank-Nicolson method with $h = 1$ to the initial value problem
$$\mathbf{q}' = \begin{pmatrix} 0 & 1 \\ -1 & -2 \end{pmatrix} \mathbf{q} + \begin{pmatrix} 0 \\ 2 \end{pmatrix}$$ with $\mathbf{q}(0) = \begin{pmatrix} 1 \\ 1 \end{pmatrix}$.

### Task 8 (5 points)

Write down the method that corresponds to the Butcher scheme
$$\begin{array}{c|cc}
0 & \alpha & -\alpha \\
1 & \alpha & \alpha \\
\hline
& \alpha & \alpha
\end{array}$$
with $\alpha = \frac{1}{2}$. Determine the step function $\rho(\mu)$ for this method.

### Task 9 (Additional, 3 points)

Briefly describe the concepts of consistency and convergence of a numerical method for solving initial value problems. What is the relationship between them?

---
## Klausur Ingenieurmathematik VI

**Bearbeitungszeit:** 90 Minuten  
**Hilfsmittel:** ein beschriebenes A4-Blatt, Taschenrechner

### Aufgabe 1 (5 Punkte)

Bestimmen Sie mittels Lagrange-Interpolation ein Interpolationspolynom durch die Punkte $(1, 1)^T$, $(2, 0)^T$ und $(3, -3)^T$.

### Aufgabe 2 (5 Punkte)

Bestimmen Sie mit der Keplerschen Fassregel eine Näherung von $\int_0^{\pi} \sin \frac{x}{2} dx$, und schätzen Sie den Quadraturfehler ab.

### Aufgabe 3 (5 Punkte)

Nähern Sie das Integral $\int_0^1 x^2 dx$ mittels der summierten Trapezregel für $J = 1$, $J = 2$ und $J = 4$ für äquidistante Stützstellen an, und führen Sie zwei Schritte der Romberg-Extrapolation aus.

### Aufgabe 4 (5 Punkte)

Bestimmen Sie mit dem zentralen Differenzenquotienten zweiter Ordnung mit $h = 0.1$ eine Näherung für die zweite Ableitung von $f(x) = x^2$ an der Stelle $x_0 = 1$. Warum erhalten Sie einen fehlerfreien Wert?

### Aufgabe 5 (5 Punkte)

Führen Sie zwei Schritte des Newton-Verfahrens zur Bestimmung einer Nullstelle von $f(x) = x^2$ mit dem Startwert $x_0 = 1$ aus. Welche Konvergenzordnung beobachten Sie? Welche allgemeinen Aussagen über die Konvergenzordnung des Newton-Verfahrens gibt es?

### Aufgabe 6 (5 Punkte)

Führen Sie einen Schritt des Euler-Heun-Verfahrens zur Lösung des Anfangswertproblems $y' = t - ty$, $y(0) = 2$ mit der Schrittweite $h = 0.2$ aus.

### Aufgabe 7 (5 Punkte)

Wenden Sie einen Schritt des Crank-Nicolson-Verfahrens mit $h = 1$ auf das Anfangswertproblem
$\mathbf{q}' = \begin{pmatrix} 0 & 1 \\ -1 & -2 \end{pmatrix} \mathbf{q} + \begin{pmatrix} 0 \\ 2 \end{pmatrix}$ mit $\mathbf{q}(0) = \begin{pmatrix} 1 \\ 1 \end{pmatrix}$ an.

### Aufgabe 8 (5 Punkte)

Notieren Sie das Verfahren, welches zum Butcher-Schema 
$\begin{array}{c|cc}
0 & \alpha & -\alpha \\
1 & \alpha & \alpha \\
\hline
 & \alpha & \alpha
\end{array}$ mit $\alpha = \frac{1}{2}$ gehört. Bestimmen Sie die Schrittfunktion $\rho(\mu)$ zu diesem Verfahren.

### Aufgabe 9 (Zusatz, 3 Punkte)

Beschreiben Sie kurz die Begriffe Konsistenz und Konvergenz eines numerischen Verfahrens zur Lösung von Anfangswertproblemen. Welcher Zusammenhang besteht zwischen ihnen?