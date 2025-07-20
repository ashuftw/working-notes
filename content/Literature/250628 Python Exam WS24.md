---
title: Python Exam WS24
draft: true
tags: 
date: 2025-06-28
---

## Exercise 1: Plotting (20 Points)

You are a research assistant analyzing various polymers as part of your research. For material analysis, you use Differential Scanning Calorimetry (DSC). In this method, temperature (in °C) and heat flow (in mW) are recorded while the samples are heated. This allows characteristic material properties to be identified.

$$
\text{DSC Curve Diagram}
$$

![[../Files/Pasted image 20250628164111.png]]

### Tasks:

a) Read the two measurement series "dsc_pp.csv" and "dsc_pe.csv" and plot them using the Matplotlib library. The polypropylene (PP) data should be displayed with a solid line and the polyethylene (PE) data with a dash-dot line. Label the axes appropriately and include a legend.

b) Identify the melting temperature $T_m$ and the crystallization temperature $T_c$ for both materials.

c) Mark the melting points (peaks) with red crosses and display the respective melting temperatures at appropriate locations with text boxes in the diagram.

d) Mark the crystallization points (peaks) with blue crosses and display the crystallization temperature at appropriate locations with text boxes in the diagram.

e) Calculate the melting enthalpy $\Delta H_m$ by integrating the corresponding peak areas in the DSC curve. Use a baseline for this.

f) Mark the integrated areas with a colored surface (light blue).

---

## Exercise 2: Differential Equations (20 Points)

You are an intern at the consulting firm Python Consulting and need to model the economic growth of the company SKI24 with seasonal competitive influences for their consultation. Generally, economic growth can be described based on revenue using the following differential equation (ODE):

$$
f'(t) = r \cdot f(t) - \alpha \cdot g(t)
$$

where:

- Growth rate of the company: $r$ (1/month)
- Competition influence rate: $\alpha$ (1/month)
- Competition influence function: $g(t) = k \cdot e^{-m \cdot t}$
- Competition intensity parameters: $k, m$

Time $t$ is measured in months. The initial condition is: $f(0) = f_0$.

Since competitive pressure in this industry is seasonal, it can be assumed with the following equation:

$$
m(t) = m_1 \cdot \cos\left(\frac{2\pi}{12} \cdot t\right)
$$

Where:

- Amplitude of seasonal fluctuation: $m_1$

### Tasks:

a) Define the differential equation as a function.

b) Use the `solve_ivp` function from the `scipy.integrate` module to solve the function $f(t)$ for the time period 0 to 7 years. Use the following parameters for the base solution:

- $r = 0.008$
- $\alpha = 0.4$
- $k = 100$
- $m_1 = 0.012$
- $f(0) = 5000$

c) Output the average monthly revenue over the entire simulation period as well as the months with the highest and lowest revenues in a complete sentence.

d) Create a subplot where you show the base solution and the solution for $k = 50$ in the upper diagram, and the base solution and the solution for $m_1 = 0.015$ in the lower diagram.

---

## Exercise 3: Object-Oriented Programming (20 Points)

Since elections are coming up again in Germany, Fred Herz needs your help with a study on voter turnout that should be evaluated using your Python code.

Create your code based on `basis_aufgabe_3.py`.

### Tasks:

a) Define the class `WahlAnalyse` (ElectionAnalysis). In the magic method `__init__()`, the parameters `region`, `jahre` (years), and `beteiligung` (turnout) should be passed and stored as protected attributes. While `region` indicates the name of the respective region, a list of years should be stored under `jahre`. The protected attribute `_trend` is initialized with the value `None` in the `__init__` method. Also check in the method whether the lists have the same number of entries. If this is not the case, a `ValueError` should be raised.

b) Define the magic method `__len__`, which returns the number of list elements of the attribute `jahre` when called.

c) Add the property `_trend`. Create a setter method in which a linear regression is performed using polyfit (NumPy library), which determines a first-degree polynomial based on the value pairs of years and turnout. The result of the regression should be stored in a tuple in the attribute `_trend` (slope, y-intercept of the line). The trend (`_trend`) should be updated each time the setter method is called.

d) Create a method `vorhersage(jahr)` (prediction(year)) that predicts voter turnout for a given year. An error should be output if no trend has been calculated yet.

e) Implement the method `plot_beteiligung()` (plot_turnout()) in which the voter turnouts are displayed as a bar chart. The historical voter turnouts and the predicted voter turnouts should differ in color. The prediction should be created for the year 2025.

f) Instantiate the regions GF, BS, and WOB as objects of the `WahlAnalyse` class. Politician Fred Herz would like to know which region is particularly important for his election campaign. For the meeting with him, you must first prepare histograms with which you can present the voter turnouts.

g) During the discussion, the question arises as to how long voter turnout has been recorded in Gifhorn. Be faster than your colleagues and output the answer using the length method.

---

