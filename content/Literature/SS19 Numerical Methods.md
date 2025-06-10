---
title: SS19 Numerical Methods
draft: true
tags: 
date: 2025-05-21
---

### Aufgabe 1 

Lagrange Interpolation
$f(x) = \frac{1}{x} - 1$, $x_0 = \frac{1}{2}$, $x_1 = 1$, $x_2 = 2$

Interpolationsfehler durch möglichst kleine Konstante abschätzen.

### Aufgabe 2

Quadraturformel gegeben: $Q(f) = \frac{b-a}{4}(3 \cdot f(\frac{2a+b}{3}) + f(b))$

Welche ist besser geeignet? Die oder die Mittelpunktsregel?

Intervall: $[-1, 1]$, also $a = -1$, $b = 1$.

### Aufgabe 3

Welche Konvergenzordnung hat der zentrale DQ zur Approximation der zweiten Abl. einer Fkt?

Begründe, welche KO es nach zwei Romberg Schritten hat.
Grundidee Romberg?

### Aufgabe 4

An verbesserten Euler-Verfahren zeigen, wie ESV hergeleitet werden + Schritte erklären.

### Aufgabe 5

$$f(x) = x^3 - 8 - x^2$$

$$g(x) = 2x^2$$

Newton Verfahren zur Bestimmung des Schnittpunkts aufstellen.
Diskutieren Sie die Konvergenzordnung.

### Aufgabe 6

Zeigen Sie, dass das Crank-Nicolson-Verfahren A-stabil ist.

## Aufgabe 7

$$y_{i+1} = y_i + h \cdot \Phi(t, y, h)$$

$$\Phi(t,y,h) = a \cdot f(t,y) + b \cdot f(t + c \cdot h, y + d \cdot h \cdot f(t,y))$$

Bedingungen für $a, b, c, d$, damit das Verfahren die Konsistenzordnung zwei hat.

### Aufgabe 8

Schwingungsgleichung (nicht angegeben als Formel) mit homogenen Dirichlet Randbedingungen. $x \in (0, \pi)$

Linienmethode anwenden und in ein System 1ter Ordnung wandeln. Vorgehen erklären.

### Aufgabe 9

Anhand des Verfahrens aus Aufgabe 7 erklären, wie Butcher Tableau aufgestellt wird.