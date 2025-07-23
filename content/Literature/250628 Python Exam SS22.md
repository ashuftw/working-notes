---
title: Python Exam SS22
draft: true
tags: 
date: 2025-06-28
---
## Exercise 1: Plotting and Interpolation (15 Points)

A colleague from aerodynamics has provided you with the contour of an airfoil profile as data points. In the file `F15_10.DAT` you will find the x and y coordinates of the profile contour. For further calculations, you want to read the profile contour with Python and display it in various ways. Proceed as follows:

### Tasks:

a) Read the data `F15_10.DAT` using NumPy and save it in an array.

b) Plot the profile using Matplotlib and label the axes. Use the `equal` option for the axes to display the profile without distortion.

c) Split the profile at the nose (x=0, y=0) and save the two parts separately as upper and lower shells. Plot the upper shell as a red line and the lower shell as a green line in your diagram. The axes should continue to be displayed without distortion.

d) Plot the area between the upper and lower shells using the `fill_between` function from the Pyplot library. For this purpose, the arrays of the upper and lower shells must have the same size. Therefore, first interpolate the profile contour of the upper and lower shells using the `interp` function from the NumPy library. Ensure an appropriately high resolution for the interpolation. Now plot the area between the curves using the `fill_between` function.

---

## Exercise 2: Vibration Damper (20 Points)

A manufacturer of machine tools wants to attach a control box to an injection machine. For technical reasons, this must be attached to the moving part of the tool. During a cycle, this moves abruptly 10cm to the left and right (rectangular function). It holds the positions for 50s each. The manufacturer has cheaply ordered a wireless sensor system from Wish to save money. Surprisingly, this works exceptionally well as long as the component moves little and the sensor remains in the original housing. Unfortunately, the connection of the housing to the machine is weakly damped and therefore oscillates for a long time. As an aspiring, clever engineer, you immediately realize that a damper can be used to reduce the vibration. However, the manufacturer wants to observe the effect live compared to the previous state. For this reason, you have attached a dynamic coupling between the masses. This can be dynamically opened or closed.
![[../Files/Pasted image 20250628164856.png|center|800]]
### Given Parameters:

- $m_1 = 1$; $c_1 = 10$; $d_1 = 0.001$; $m_2 = 0.01$; $c_2 = ?$; $d_2 = 0.005$

### Equations of Motion:



$$
c_1u = m_1\ddot{x}_1 + (d_1 + d_2)\dot{x}_1 - d_2\dot{x}_2 + (c_1 + (c_2 + c_3))x_1 - (c_2 + c_3)x_2
$$




$$
0 = m_2\ddot{x}_2 - d_2\dot{x}_1 + d_2\dot{x}_2 - (c_2 + c_3)x_1 + x_2(c_2 + c_3)
$$



### Tasks:

a) Implement the equation of motion in the form of a differential equation. **Tip:** (For damping: $c_1/m_1 = c_2/m_2$)

b) Use `solve_ivp` for numerical solution of the equation of motion for 600s. Use a high stiffness (10000 N/m) for the dynamic coupling ($c_3$) in the first 300s and deactivate the coupling afterwards.

c) Display the motion of both masses in two subplots one above the other. Label all axes.

d) **Bonus:** Generate the change in position of the base point $u$ as a function of time in a single line.

---

## Exercise 3: Object-Oriented Programming (15 Points)

During the Corona pandemic, restaurants have to deal with constant changes in legal regulations. To simplify operations, a large franchise chain has commissioned you to develop visitor management software. The program should allow customer check-in and calculate occupancy considering current regulations. For this, customers must check in with a digital vaccination passport. The vaccination passport will be provided to you by the federal government.

### Tasks:

a) Define the class `Restaurant`. In the magic method `__init__()`, the parameters `name`, `seats`, and `area` should be passed and stored as protected attributes. Furthermore, the protected attribute `customers` should be initialized with the value 0.

b) Add the properties `customers` and `seats` to the class.

c) Write the method `activate_new_regulation()`, in which the number of seats is reset based on the passed parameter `min_area_per_customer`. Note that there are only complete customers.

d) Write the method `check_in()`, which receives a vaccination passport as a parameter. As long as the vaccination passport allows entry and there are still seats available in the restaurant, a seat should be allocated and the message "Access Granted" should be output. If no more seats are available, the message "Restaurant already full" should be output. If the vaccination passport denies entry, the message "Access Denied" should be output.

e) Import the function `create_customers()` from the given library `impfpass` and use it to create a list with 60 vaccination passports.

f) Create the two restaurants "Jolly Banana Time" and "Sad Banana Time". Both restaurants have 60 seats in a 100 m² dining room. Activate a new legal regulation for the restaurant "Sad Banana Time" that requires at least 10 m² of space for each customer.

g) Check in all customers at both restaurants. Return the occupancy of both restaurants and their maximum capacity in a formatted string.

---
