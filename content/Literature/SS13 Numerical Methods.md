---
title: SS13-Past-Exam
draft: true
tags: 
date: 2025-05-21
---

# Klausur Modellierung und Numerik von Differentialgleichungen (Wdh.)

**Bearbeitungszeit:** 90 Minuten  
**Hilfsmittel:** ein beschriebenes A4-Blatt, ein nicht internetfähiger Taschenrechner

### Aufgabe 1 (5 Punkte): 

Sie wollen eine unbekannte Funktion auf dem Intervall $[-2, 2]$ durch ein Polynom dritten Grades an den Stützstellen $\left(-2, \begin{pmatrix} -5 \end{pmatrix}\right)$, $\left(-1, \begin{pmatrix} 0 \end{pmatrix}\right)$, $\left(0, \begin{pmatrix} -1 \end{pmatrix}\right)$, $\left(2, \begin{pmatrix} 3 \end{pmatrix}\right)$ annähern. Geben Sie mit Hilfe der Lagrange-Interpolation das Polynom an, und schätzen Sie den Interpolationsfehler ab.

### Aufgabe 2 (5 Punkte): 

Wenden Sie die Trapez- und die Fassregel zur Auswertung des Integrals $\int_{-2}^{2} x^3 - 2x - 1 \, dx$ an. Schätzen Sie jeweils den Quadraturfehler ab.

### Aufgabe 3 (5 Punkte): 

Konstruieren Sie unter Verwendung des Romberg-Schemas einen zweiseitigen Differenzenquotienten mit Konvergenzordnung 4 zur Annäherung der ersten Ableitung einer Funktion $f$ an der Stelle $x$.

### Aufgabe 4 (5 Punkte): 

Bestimmen Sie eine Näherungslösung der Gleichung $x - 2\ln x = 1$ mit Hilfe der Banach-Iteration. Finden Sie dafür ein Intervall und eine Iterationsvorschrift, die den Voraussetzungen des Banachschen Fixpunktsatzes genügen und führen Sie mit einem geeignet gewählten Startwert zwei Schritte der Banach-Iteration aus. Schätzen Sie a priori den Fehler ab.

### Aufgabe 5 (5 Punkte): 

Wenden Sie einen Schritt des Crank-Nicolson-Verfahrens mit $h = 1$ auf das Anfangswertproblem $q' = \begin{pmatrix} -3 & 2 \\ 1 & -2 \end{pmatrix} q + \begin{pmatrix} 1 \\ 2 \end{pmatrix}$ mit $q(0) = \begin{pmatrix} 1 \\ 1 \end{pmatrix}$ an.

### Aufgabe 6 (5 Punkte): 

Führen Sie einen Schritt des Euler-Heun-Verfahrens mit der Schrittweite $h = 0.1$ zur numerischen Lösung des Anfangswertproblems $y'(t) = -10y - \sin t$, $y(0) = 1$ aus. Welche Schrittweite sollten Sie maximal wählen, wenn Sie das Euler-Heun-Verfahren zur Lösung verwenden? Erläutern Sie dazu kurz den Begriff steife Differentialgleichung.

### Aufgabe 7 (5 Punkte): 

Berechnen Sie mittels des zweistufigen Adams-Bashforth-Verfahren mit Schrittweite $h = 0.1$ eine numerische Näherung von $y(1.2)$ mit $y' = -2ty$, $y(1) = 1$. Verwenden Sie zur Initialisierung das einstufige Adams-Bashforth-Verfahren.

### Aufgabe 8 (5 Punkte): 

Geben Sie mit Hilfe des expliziten Euler-Verfahrens ein Finite-Differenzen-Schema an, um die Gleichung $\frac{\partial u}{\partial t} = \frac{\partial}{\partial x}\left((1+x)\frac{\partial u}{\partial x}\right)$ zu lösen.

### Zusatzaufgabe (3 Punkte): 

Erläutern Sie die CFL-Bedingung.