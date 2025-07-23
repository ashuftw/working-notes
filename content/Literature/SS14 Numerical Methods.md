---
title: SS14 Numerical Methods
draft: true
tags: 
date: 2025-05-21
---
**Completion time:** 90 minutes
**Permitted resources:** are a written/printed A4 sheet of paper and a non-internet-enabled calculator. Calculations and solutions must be clearly documented.

### Task 1 (5 points):

Using Lagrange interpolation, determine a polynomial that agrees with the function $f(x) = \cos x$ at the interpolation points $x_0 = -\frac{\pi}{4}$, $x_1 = 0$, and $x_2 = \frac{\pi}{4}$. What deviation do you expect when using the interpolation polynomial to approximate $\cos \frac{\pi}{8}$?

### Task 2 (5 points):

Explain which quadrature formula is generally better suited for numerical integration: the quadrature formula $Q(f) = \frac{b-a}{4}\left(3f\left(\frac{2a+b}{3}\right) + f(b)\right)$ or the well-known trapezoidal rule?

### Task 3 (5 points):

Using the Taylor expansion, determine the order of convergence of the two-sided difference quotient $f''(x) \approx \frac{2f(x-3h) - 5f(x) + 3f(x+2h)}{15h^2}$.

### Task 4 (5 points):

Using the iteration rule $x_{k+1} = 1+3\ln x_k$, a solution to the equation $x - 3\ln x = 1$ can be determined. From which of the intervals $D_0 = [1,7]$, $D_1 = [4,6]$, $D_2 = [6,7]$ should you choose a starting value for your iteration to obtain a unique solution? How many iteration steps do you need to perform to determine the solution to three decimal places, starting from the starting value $x_0 = 6$?

### Task 5 (5 points):

Apply one step each of the explicit and implicit Euler method with $h = 1$ to $q' = \begin{pmatrix} -2 & 1 \\ 0 & -2 \end{pmatrix} q + \begin{pmatrix} 1 \\ 2 \end{pmatrix}$ with $q(0) = \begin{pmatrix} 1 \\ 1 \end{pmatrix}$. Do you expect qualitatively correct solutions? What is the maximum step size you should choose when using the methods for the solution?

### Task 6 (5 points):

Using the two-stage BDF method with a step size of $h = 0.1$, calculate a numerical approximation of $y(2.2)$ with $y' = y - t$, $y(2) = 3$. Use the one-stage BDF method for initialization.

### Task 7 (5 points):

Is the method with the Butcher scheme


$$
\begin{array}{c|cc}
& 0 & \frac{1}{2} & 0 \\
& 1 & \frac{1}{2} & 0 \\
\hline
& & \frac{1}{2} & \frac{1}{2}
\end{array}
$$


A-stable?

### Task 8 (5 points):
Apply the difference method with step size $h = \frac{1}{2}$ to the boundary value problem $(1 + x^2)u'' - xu' + 4u = 0$, $u(-1) = u(1) = 1$. Note the resulting system of linear equations. You do not need to solve this system.

### Additional task (5 points):
A suitable finite difference method for solving equations of the form $u_t = -au_{xx}$, $a > 0$, is obtained by first setting up the time Taylor expansion of the function $u$ to degree 2, then replacing the terms $u_t$ and $u_{tt}$ with position derivatives using the partial differential equation, and finally approximating these numerically using central difference quotients. State this procedure.

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



$$
\begin{array}{c|cc}
 & 0 & \frac{1}{2} & 0 \\
 & 1 & \frac{1}{2} & 0 \\
\hline
 & & \frac{1}{2} & \frac{1}{2}
\end{array}
$$


A-stabil?

### Aufgabe 8 (5 Punkte): 
Wenden Sie das Differenzen-Verfahren mit Schrittweite $h = \frac{1}{2}$ auf das Randwertproblem $(1 + x^2)u'' - xu' + 4u = 0$, $u(-1) = u(1) = 1$ an. Notieren Sie das entstehende lineare Gleichungssystem. Sie brauchen dieses System nicht zu lösen.

### Zusatzaufgabe (5 Punkte): 
Ein geeignetes Finite-Differenzen-Verfahren, zur Lösung von Gleichungen der Form $u_t = -au_{xx}$, $a > 0$, erhält man, indem man zunächst die zeitliche Taylor-Entwicklung der Funktion $u$ zum Grad 2 aufstellt, dort mittels der partiellen Differentialgleichung die Terme $u_t$ und $u_{tt}$ durch Ortsableitungen ersetzt und diese schließlich mit zentralen Differenzenquotienten numerisch approximiert. Geben Sie diese Verfahrensvorschrift an.