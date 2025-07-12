---
title: SS18 Numerical Methods
draft: true
tags: 
date: 2025-05-21
---
## Engineering Mathematics VI Exam

### Numerical Analysis and Modeling with Differential Equations

**Completion time:** 90 minutes
**Tools:** Predefined formula collection

### Task 1 (5 points)

Using Lagrange interpolation, determine a polynomial $p$ through the points $(x_i, f(x_i))$, $i = 0, 1, 2$ for $f(x) = \cos(\pi x)$ and $x_0 = -1$, $x_1 = 0$, and $x_2 = \frac{1}{2}$. Estimate the interpolation error in the interval $[-1, 1]$ using the smallest possible constant.

### Task 2 (5 points)

Determine the order of convergence of the central difference quotient as an approximation of the first derivative of a function. Establish the first step of the Romberg scheme. Explain the basic idea of ​​the Romberg scheme. State the order of convergence after three steps of the Romberg scheme.

### Task 3 (5 points)

Derive the Crank-Nicolson method. Use it to explain the basic idea of ​​constructing one-step methods.

### Task 4 (5 points)

Determine the order of consistency of $y_{i+1} = y_i + \frac{h}{2}[f(t_i, y_i) + f(t_{i+1}, y_i + hf(t_i, y_i))]$ and prove it. Write the method as a Butcher tableau.

### Task 5 (5 points)

Define Newton's method to determine the minimum of $f(x) = \frac{1}{3}x^3 - 5x^2 + 7x$. Provide a reasoned explanation for the order of convergence. Explain whether Newton's method is well-suited for this problem.

### Task 6 (5 points)

Consider the system $\dot{q}(t) = -\begin{pmatrix} 1 & 700 \\ 0 & 2 \end{pmatrix}q(t)$ with $q(0) = (1, 1)^T$. Derive the maximum step size of the explicit Euler method for solving this differential equation. State properties of the system.

### Task 7 (5 points)

Explain the finite difference method using the example of the heat conduction equation $u_t = 3u_{xx}$ for $x \in (-1, 1)$ with homogeneous Neumann boundary conditions and $u(0, x) = u_0(x)$, $x \in (-1, 1)$. Briefly explain the difference from the line method.

### Task 8 (5 points)

Explain the terms convergence, consistency, and stability of a one-step method. Explain the relationship between the three terms. What consequence follows from the A-stability of a method?

### Task 9 (Additional, 3 points)

Prove the convergence order of the Banach fixed-point iteration. Under what conditions does the sequence converge to the fixed point?

---
## Klausur Ingenieurmathematik VI

### Numerik und Modellierung mit Differentialgleichungen

**Bearbeitungszeit:** 90 Minuten  
**Hilfsmittel:** vorgegebene Formelsammlung

### Aufgabe 1 (5 Punkte)

Bestimmen Sie mit der Lagrange-Interpolation ein Polynom $p$ durch die Punkte $(x_i, f(x_i))$, $i = 0, 1, 2$ für $f(x) = \cos(\pi x)$ und $x_0 = -1$, $x_1 = 0$ und $x_2 = \frac{1}{2}$. Schätzen Sie den Interpolationsfehler im Intervall $[-1, 1]$ durch eine möglichst kleine Konstante ab.

### Aufgabe 2 (5 Punkte)

Bestimmen Sie die Konvergenzordnung des zentralen Differenzenquotienten als Approximation der ersten Ableitung einer Funktion. Stellen Sie den ersten Schritt des Romberg-Schemas auf. Erklären Sie die Grundidee des Romberg-Schemas. Geben Sie die Konvergenzordnung nach 3 Schritten des Romberg-Schemas an.

### Aufgabe 3 (5 Punkte)

Leiten Sie das Crank-Nicolson-Verfahren her. Erklären Sie daran die Grundidee der Konstruktion von Einschrittverfahren.

### Aufgabe 4 (5 Punkte)

Bestimme Sie die Konsistenzordnung von $y_{i+1} = y_i + \frac{h}{2}[f(t_i, y_i) + f(t_{i+1}, y_i + hf(t_i, y_i))]$ und weisen Sie diese nach. Schreiben Sie das Verfahren als Butcher-Tableau.

### Aufgabe 5 (5 Punkte)

Stellen Sie das Newton-Verfahren zur Bestimmung des Minimums von $f(x) = \frac{1}{3}x^3 - 5x^2 + 7x$ auf. Geben Sie begründet die Konvergenzordnung an. Begründen Sie, ob das Newton-Verfahren für dieses Problem gut geeignet ist.

### Aufgabe 6 (5 Punkte)

Betrachten Sie das System $\dot{q}(t) = -\begin{pmatrix} 1 & 700 \\ 0 & 2 \end{pmatrix}q(t)$ mit $q(0) = (1, 1)^T$. Leiten Sie die maximale Schrittweite des expliziten Euler-Verfahrens zum Lösen dieser Differentialgleichung her. Geben Sie Eigenschaften des Systems an.

### Aufgabe 7 (5 Punkte)

Erklären Sie die Finite-Differenzen-Methode am Beispiel der Wärmeleitungsgleichung $u_t = 3u_{xx}$ für $x \in (-1, 1)$ mit homogenen Neumann-Randbedingungen und $u(0, x) = u_0(x)$, $x \in (-1, 1)$. Erklären Sie kurz den Unterschied zur Linienmethode.

### Aufgabe 8 (5 Punkte)

Erläutern Sie die Begriffe Konvergenz, Konsistenz und Stabilität eines Einschrittverfahrens. Erklären Sie den Zusammenhang zwischen den drei Begriffen. Welche Folgerung ergibt sich aus der A-Stabilität eines Verfahrens?

### Aufgabe 9 (Zusatz, 3 Punkte)

Weisen Sie die Konvergenzordnung der Banachschen Fixpunktiteration nach. Unter welchen Bedingungen konvergiert die Folge gegen den Fixpunkt?