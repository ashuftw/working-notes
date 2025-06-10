---
title: SS14 Numerical Methods
draft: true
tags: 
date: 2025-05-21
---

**Bearbeitungszeit:** 90 Minuten  
**Zugelassene Hilfsmittel:** sind ein beschriebenes/bedrucktes A4-Blatt und ein nicht internetfähiger Taschenrechner. Rechen- und Lösungswege müssen nachvollziehbar dokumentiert werden.

### Aufgabe 1 (5 Punkte): 

Bestimmen Sie mit Hilfe der Lagrange-Interpolation ein Polynom, welches an den Stützstellen $x_0 = -\frac{\pi}{4}$, $x_1 = 0$, $x_2 = \frac{\pi}{4}$ mit der Funktion $f(x) = \cos x$ übereinstimmt. Welche Abweichung erwarten Sie, wenn Sie das Interpolationspolynom zur Annäherung von $\cos \frac{\pi}{8}$ verwenden?

### Aufgabe 2 (5 Punkte): 

Begründen Sie welche Quadraturformel sich im Allgemeinen besser zur numerischen Integration eignet, die Quadraturformel $Q(f) = \frac{b-a}{4}\left(3f\left(\frac{2a+b}{3}\right) + f(b)\right)$ oder die bekannte Trapezregel?

### Aufgabe 3 (5 Punkte): 

Bestimmen Sie mittels der Taylor-Entwicklung die Konvergenzordnung des zweiseitigen Differenzenquotienten $f''(x) \approx \frac{2f(x-3h) - 5f(x) + 3f(x+2h)}{15h^2}$.

### Aufgabe 4 (5 Punkte): 

Mit Hilfe der Iterationsvorschrift $x_{k+1} = 1+3\ln x_k$ lässt sich eine Lösung der Gleichung $x - 3\ln x = 1$ bestimmen. Aus welchem der Intervalle $D_0 = [1,7]$, $D_1 = [4,6]$, $D_2 = [6,7]$ sollten Sie einen Startwert für Ihre Iteration wählen, um eine eindeutige Lösung zu erhalten? Wie viele Schritte der Iteration müssen Sie ausführen, um vom Startwert $x_0 = 6$ ausgehend die Lösung bis auf drei Nachkommastellen genau zu bestimmen.

### Aufgabe 5 (5 Punkte): 

Wenden Sie je einen Schritt des expliziten und des impliziten Euler-Verfahrens mit $h = 1$ auf $q' = \begin{pmatrix} -2 & 1 \\ 0 & -2 \end{pmatrix} q + \begin{pmatrix} 1 \\ 2 \end{pmatrix}$ mit $q(0) = \begin{pmatrix} 1 \\ 1 \end{pmatrix}$ an. Erwarten Sie qualitativ richtige Lösungen? Welche Schrittweite sollten Sie jeweils maximal wählen, wenn Sie die Verfahren zur Lösung verwenden?

### Aufgabe 6 (5 Punkte): 

Berechnen Sie mittels des zweistufigen BDF-Verfahrens mit der Schrittweite $h = 0.1$ eine numerische Näherung von $y(2.2)$ mit $y' = y - t$, $y(2) = 3$. Verwenden Sie zur Initialisierung das einstufige BDF-Verfahren.

### Aufgabe 7 (5 Punkte): 

Ist das Verfahren mit dem Butcher Schema 

$$\begin{array}{c|cc}
 & 0 & \frac{1}{2} & 0 \\
 & 1 & \frac{1}{2} & 0 \\
\hline
 & & \frac{1}{2} & \frac{1}{2}
\end{array}$$
A-stabil?

### Aufgabe 8 (5 Punkte): 
Wenden Sie das Differenzen-Verfahren mit Schrittweite $h = \frac{1}{2}$ auf das Randwertproblem $(1 + x^2)u'' - xu' + 4u = 0$, $u(-1) = u(1) = 1$ an. Notieren Sie das entstehende lineare Gleichungssystem. Sie brauchen dieses System nicht zu lösen.

### Zusatzaufgabe (5 Punkte): 
Ein geeignetes Finite-Differenzen-Verfahren, zur Lösung von Gleichungen der Form $u_t = -au_{xx}$, $a > 0$, erhält man, indem man zunächst die zeitliche Taylor-Entwicklung der Funktion $u$ zum Grad 2 aufstellt, dort mittels der partiellen Differentialgleichung die Terme $u_t$ und $u_{tt}$ durch Ortsableitungen ersetzt und diese schließlich mit zentralen Differenzenquotienten numerisch approximiert. Geben Sie diese Verfahrensvorschrift an.