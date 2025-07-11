---
title: Python Exam SS23
draft: true
tags: 
date: 2025-06-28
---
## Task 1: Plotting and Fitting (20 Points)

The opioid crisis, a serious health challenge, has led to an alarming increase in drug-related deaths in the USA. In this task, you will analyze data on drug deaths in the USA and create a predictive model to gain insights into the development of deaths related to fentanyl overdoses.

a) Import the data on drug deaths in the USA from 1990 to 2020. This data is available in the file **"od_deaths_usa.csv"**.

b) Create a plot showing the total number of deaths and the number of fentanyl-related deaths from drug overdoses. Use a blue line for the total number of deaths and a red line for fentanyl-related deaths. Label the axes, add a legend, and enable the grid.

c) Fit the following function to the data using the **`curve_fit`** method from the **`scipy.optimize`** library. Use as starting values $a = 1$ and $b = 2000$:


$$
f(x, a, b) = \exp(a \cdot (x - b))
$$


d) Add the prediction model to the plot as a dashed line in the same color as the corresponding curve. Use the period from 1975 to 2025 for the prediction. Display the parameter values $a$ and $b$ of the model in the legend.

e) Based on your prediction model: How many deaths related to fentanyl overdoses are expected in the USA in 2023 and in 2030? Output your answer as a formatted string.

f) In which year are more deaths due to fentanyl overdoses expected to occur than deaths from total overdoses? Consider the period from 2010 to 2025.

---

## Task 2: Modeling a Predator-Prey System (20 Points)

The predator-prey model describes the interaction between two populations, where one acts as predator and the other as prey. In this task, we consider the model with foxes as predators and rabbits as prey. The model can be described by the following differential equations:


$$
\frac{dH}{dt} = aH - bFH
$$



$$
\frac{dF}{dt} = -cF + dHF
$$


Where $H$ is the population size of rabbits, $F$ is the population size of foxes, $a$ is the growth rate of rabbits, $b$ is the rate at which foxes eat rabbits, $c$ is the natural mortality rate of foxes, and $d$ is the rate at which foxes feed and reproduce.

a) Solve the differential equation system using **`solve_ivp`** from the **`scipy.integrate`** library. Use the initial conditions $H_0 = 100$ and $F_0 = 20$. Calculate the population development for a period from 0 to 100 years. Use the given parameters $a = 0.03$, $b = 0.001$, $c = 0.1$, and $d = 0.002$. Use the **Radau-solver** for the solution.

b) Plot the result in a subplot with two plots stacked on top of each other. In the upper plot, the development of the rabbit population $H$ should be displayed as a blue line and the development of the fox population $F$ as a red line. In the lower plot, the change in population sizes over time should be displayed, where the change in rabbit population should be displayed as a blue dashed line and the change in fox population as a red dashed line. Enable the grid for all plots.

c) Determine the influence of the rabbit growth rate on the predator-prey system. Vary the growth rate $a$ in the range from 0.01 to 0.1 with an interval of 0.01. For each growth rate, the population developments of rabbits and foxes should be calculated over a period from 0 to 15 years.

d) Plot the final values of the population sizes of rabbits and foxes versus the growth rate $a$. Use X-markers for the data points and connect them with a dashed line.

---

## Task 3: Object-Oriented Programming (20 Points)

For the preliminary design of rotor blades for wind turbines, you should write a program for optimizing beams. For this, you need a class that processes the mechanical and geometric properties of a beam. The rotor blades should be approximately modeled as cantilever beams under line load. For optimization, in addition to the geometric parameters, the maximum stress in the beam and the maximum deflection are crucial.

Given are the following formulas:


$$
w_{max} = \frac{ql^4}{8EI}
$$



$$
\sigma_{max} = \frac{M_b}{W_b}
$$



$$
M_b = -\frac{ql^2}{2}
$$



$$
W_b = \frac{I}{z_{max}}
$$


a) Define a class **`Beam`** with the magic method **`__init__`,** which takes the parameters **`modulus`, `inertia`, `length`, `z_max`,** and **`load`**. Store all parameters in protected attributes.

b) Define the property `inertia` with a setter to access the protected attribute **`_inertia`**.

c) Implement the properties **`sigma_max`** and **`w_max`**, which return the maximum stress in the beam $\sigma_{max}$ as the ratio of $M_b$ and $W_b$ as well as the end deflection $w_{max}$ of the beam depending on the current area moment of inertia $I$.

d) Define the function **`inertia_i_beam`**, which calculates the area moment of inertia of an I-beam as a function of the width $b$, height $h$, web width $t$, and flange height $a$.

e) Use the given parameters $b = 0.3m$, $h = 1.5m$, $t = 0.02m$, and $a = 0.05m$ to calculate the area moment of inertia. Instantiate an object of the class **`Beam`** with a length $l = 80m$, a modulus $E = 90GPa$, and a line load of $q = 1500N/m$. Use the Beam object to output the maximum stress $\sigma_{max}$ and the maximum deflection $w_{max}$ of the beam in a formatted string.