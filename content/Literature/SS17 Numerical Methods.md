---
title: SS17 Numerical Methods
draft: true
tags: 
date: 2025-05-21
---
## Numerik und Modellierung mit Differentialgleichungen

**Bearbeitungszeit:** 90 Minuten  
**Hilfsmittel:** vorgegebene Formelsammlung

### Aufgabe 1 (5 Punkte)
Bestimmen Sie mit der Lagrange-Interpolation ein Polynom $p$ durch die Punkte $(x_i, f(x_i))$, $i = 0, 1, 2$ für $f(x) = x^3$ und $x_0 = -1$, $x_1 = 0$ und $x_2 = 1$. Schätzen Sie den Interpolationsfehler im Intervall $[-1, 1]$ durch eine möglichst kleine Konstante ab.

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