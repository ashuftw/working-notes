---
title: Python Exam WS23
draft: true
tags: 
date: 2025-06-28
---

## Task 1: Solving Equations and Plotting (15 Points)

The relative density (rd) of Gyroid structures can be approximately determined using the following relationship:

$$rd = 3x - 4(x)^3 \text{ with } x = t/l$$

Where t is the wall thickness in mm and l is the length of a unit cell in mm. For the preliminary design of such a structure, you want to calculate the wall thickness t as a function of the unit cell length l for a specific relative density rd.

a) First, rearrange the equation so that the left side equals zero and write a function `tl_ratio(x)` that returns the ratio of wall thickness to unit cell length $x$ for a specific relative density.

b) Use the `newton` function from the `scipy.optimize` library to determine the ratio $t/l$ for a relative density of $rd = 0.05$. Choose $x_0 = 0.1$ as the starting value. Now calculate the wall thickness t for a unit cell length $l = 22.5$.

c) Write the function `wall_thickness(rd, l)` that returns the wall thickness as a function of the unit cell length and the relative density.

d) Plot the wall thickness versus the unit cell length in the interval $l = [5, 40]$ and for the relative densities $rd = (0.25, 0.50, 0.75, 1.00)$. Label the axes and assign each curve its relative density in the legend. Use a formatted string for this purpose.

---

## Task 2: Vibration Damper (20 Points)

Your supervisor wants to evaluate complex differential equations for electrical systems. He is an old theoretician and is very good at setting up the differential equations on paper but has no knowledge of Python at all. For this reason, he needs your help to numerically calculate a rough estimate of the impedance. Since your supervisor generally distrusts numerical solutions, he first wants a test with a very simple series resonant circuit. The series resonant circuit with forced oscillation has the differential equation:

$$2\pi f\hat{U} \sin(2\pi f \cdot t) = L\ddot{I} + R\dot{I} + \frac{I}{C}$$

The resonant circuit should have the following parameters (pay attention to units!):

$$\hat{U} = 1V$$ $$R = 1\Omega$$ $$C = 1mF$$ $$L = 10mF$$

a) Use the `solve_ivp` function from the `scipy.integrate` library to solve the differential equation between 0 and 0.3 seconds. Pass the target frequency $f = 10$ Hz as an argument via `args`. Use (0,0) as initial values for current $I$ and current rate of change $\dot{I}$.

b) Check 100 frequencies with evenly logarithmic spacing from $f = 10Hz$ to $f = 100Hz$. Simulate 0.3s of the system's current response and evaluate the last 0.1s. Form the magnitude of the impedance Z for each frequency using the equation:

$$|Z| = \frac{2\hat{U}}{I_{max} - I_{min}}$$

c) Plot the reciprocal of the impedance $1/|Z|$ versus frequency in a graph. Label all axes.

---

## Task 3: Object-Oriented Programming (15 Points)

As an aspiring engineer, you repeatedly need to plot simple two-dimensional functions. Since you no longer want to create these plots manually in the future, you write yourself a plot class:

a) Define the class `FunctionPlot`. In the magic method `__init__()`, the parameters `func`, `limits`, and `args` should be passed and stored as protected attributes. While `limits` is passed with the default value `(0, 1)`, `args` is passed with the default value `None`. The protected attribute `label` is defined in the `__init__` method with the name of the passed function.

b) Add the properties `x` and `y` to the class. The property `x` should return a one-dimensional array with 50 equally distributed values within the boundaries of `self._limits`. The property `y` should return the function values of `self._func` at positions `x`. If additional function arguments for `self._func` are present, they should be considered during function evaluation.

c) Write the method `plot()`, in which the plot including legend is created using the `matplotlib.pyplot` library.

d) Write the method `show()`, in which the class's own plot method is called and the plot is displayed.

e) Define outside the class definition the function `f(x, rd=0.1)`:

$$f(x, rd = 0.1) = 3x - 4x^3 - rd$$

f) Instantiate an object of the class `FunctionPlot` with the function `f` and plot it in the range `(0, 0.1)` with the method `show()`.

g) Pass the new relative density `rd=0.01` as an additional argument. How does the plot change?