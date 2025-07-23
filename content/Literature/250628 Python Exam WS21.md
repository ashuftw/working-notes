---
title: Python Exam WS21
draft: true
tags: 
date: 2025-06-28
---
## Task 1: Curve Fitting (10 Points)

A research group from Biomechanics has conducted a compression experiment on a muscle cell. The file `experimentalData.csv` contains the measured force-strain data, which should be approximated by a model function. Proceed as follows:

a) Read the data `experimentalData.csv` into Python, where the strain and force values should be stored in vectors of equal length.

b) Fit a 4th order polynomial to the measurement data using `numpy.polyfit`. The normalized error of the approximation can then be calculated using the formula:



$$
e = \frac{LSE}{N \cdot F_{max}}
$$



Here, LSE stands for the Least Squares Error, which can be returned by the `numpy.polyfit` function, N for the number of measurement points, and $F_{max}$ for the measured maximum force. Output the error e in percent as a floating-point number in the console in the following format: "The 4th order polynomial has an error of XX.XX %".

c) Plot the measurement data as a gray curve and the fitted model as a black curve in a window with grid lines. Both the experimentally determined data and the model should be labeled in a legend. Additionally, the x-axis should only display values in the interval [0, 0.6]. Pay attention to a meaningful choice of axis labels.

---

## Task 2: A Simplified Model of Resin Curing (20 Points)

The curing of epoxy resins can be described by differential equations. A central parameter of this reaction is the degree of cure α, which describes how far a reaction has progressed. Here, α=1 corresponds to complete curing. Since this is an exothermic reaction, the temperature T increases during curing. The following differential equations describe the curing behavior:



$$
\frac{d\alpha}{dt} = A_1 e^{-\frac{E_1}{RT}} \alpha^m(1 - \alpha)^n
$$





$$
\frac{dT}{dt} = \frac{1}{c_P}(Q_m \frac{d\alpha}{dt} + \dot{Q_s})
$$



where $A_1 = 400 s^{-1}$, $E_1 = 18700 \frac{J}{mol}$, $m = 1.5$, $n = 1.7$ and $Q_m = 84000 \frac{J}{kg}$ are the material parameters of the epoxy resin, $R = 8.3 \frac{J}{mol \cdot K}$ is the universal gas constant, $c_P = 1100 \frac{J}{kg \cdot K}$ is the specific heat capacity of the epoxy, and $\dot{Q_s} = -142 \frac{J}{kg \cdot s}$ is a specific heat flow from the system assumed to be constant.

a) Solve the differential equation using scipy. Use as initial conditions a temperature of T=280K and a degree of cure at the beginning of α=0.01. Calculate the first 300 seconds of the reaction and choose the Runge Kutta 3(2)-solver for the solution.

b) Plot the result in the form of subplots with three plots stacked on top of each other. The top plot should show the temperature T, the middle one the degree of cure α, and the bottom one the curing rate dα/dt. Plot the temperature as a red line, the degree of cure as a blue line, and the curing rate as a green line. Enable the grid for all plots.

c) The resin curing is strongly temperature dependent. Determine this influence by varying the starting temperature of the curing reaction. Vary the temperature in the range between 270K and 350K with an interval of 10K. Determine the time after which the reaction is completely finished. The reaction is considered complete when a degree of cure of 99% is reached. Plot the time until complete curing versus the starting temperature. Individual data points should be displayed as X and connected with a dashed line.

---

## Task 3: Object-Oriented Programming (20 Points)

The area moment of inertia is a crucial parameter for the deflection of a beam. While the area moment of inertia of simple geometries can be determined analytically, numerical methods are required for complex geometries. In this task, a class "Inertia" should be created that calculates the area moments of inertia $I_y$ and $I_z$ of arbitrary geometries based on a bitmap. In the bitmap, the value 1 (white) represents the geometry, the value 0 (black) the void. The class should be used to compare the area moments of inertia of two different geometries. The geometries are shown:
![[../Files/Pasted image 20250628161721.png|center]]
Figure 1: (a) Class diagram, (b) Rectangle, (c) Gyroid and (d) Center of gravity calculation

***Hint:*** *The Inertia class should be programmed exclusively for square bitmaps with square pixels. This means for Figure 1 (b) and (c) $l_y = l_z$ and for Figure 3 (d) $d_y = d_z$. The area moment of inertia $I_y$ is determined from the sum of the area moments of inertia of the individual pixels $I_{yi}$ and the Steiner components $z_i^2 \cdot A_i$. Here $z_i$ is the z-distance of a pixel to the center of gravity. The center of gravity is given as $(y_{cog} = 10, z_{cog} = 10)$.*



$$
I_y = \sum I_{yi} + \sum z_i^2 \cdot A_i
$$





$$
I_{yi} = \frac{b_i \cdot h_i^3}{12}
$$





$$
b_i = h_i
$$




1. Define the class `Inertia`. In the magic method `__init__(self, fname, size)`, the protected attributes `_bitmap`, `_length_px`, `_area_px` and `_distance_px` should be initialized. Use the command `numpy.genfromtxt(fname)` to import a CSV file stored at the file path fname and assign the matrix to the attribute `_bitmap`. Determine the length and area of a pixel (`_length_px`, `_area_px`) from the dimension of the matrix and the edge length of the square passed through the parameter size. Now determine the y- and z-distance of each pixel center from the origin in the vector `_distance_px` ($d_{px} = d_y = d_z$ in Figure 3 (d)). Use the command `numpy.linspace()` for this.
    
2. Define the public method `show()` and use the command `imshow()` from the pyplot library to display the `_bitmap`.
    
3. Write the public method `get_inertia()`. The method should return a list with the area moments of inertia $I_y$ and $I_z$ as a return value. Make use of the attribute `_distance_px` ($d_{px}$) and the method `get_cog()` when calculating the moments.
    
4. Instantiate two objects of the class `Inertia` outside the class definition, each determining the area moment of inertia of the bitmap "rect.csv" and the bitmap "gyroid.csv". Use the `show()` method to visualize the bitmaps. Use the methods `get_cog()` and `get_inertia()` to determine the centers of gravity and area moments of inertia of the geometries. Output the results in a formatted string. Which geometry has the higher area moment of inertia in y and z direction respectively? Compare the result of "rect.csv" with an analytical calculation according to Figure 3a.