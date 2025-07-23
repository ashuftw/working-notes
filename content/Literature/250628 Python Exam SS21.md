---
title: Python Exam SS21
draft: true
tags: 
date: 2025-06-28
---
## Exercise 1: Curve Fitting (10 Points)

Given are some measurement data from a characteristic curve determination of a mechanical spring in the file "federkennlinie_klausur.csv". The first column contains the displacement in meters, the second column contains the measured force $F_c$ in Newton.

### Tasks:

1. Load the given measurement values into 2 numpy arrays and plot force versus displacement with matplotlib using green crosses.
    
2. The displayed measurement values can be approximated with the following function:
	
$$
f(x, a, b) = \frac{x}{a} \cdot \left|\tanh\left(\frac{x}{b}\right)\right|
$$

	Define this formula as a Python function. Determine optimal values for the parameters $a$ and $b$ using scipy. Display the optimal solution in the figure from task 1 with a dash-dot line. Create an appropriate legend in the bottom right of the image to distinguish between both data series. Save the optimal parameters using Python in a text file.
    
3. Create a text box using the `matplotlib.pyplot.text` command that shows the optimal parameters. Both parameters should be displayed as floating-point numbers with one decimal place. The text box should be displayed in the top left of the image. The result should look like this, where instead of "xyz" the parameters should be displayed:
    ```
    a=xyz
    b=xyz
    ```

---

## Exercise 2: Ordinary Differential Equation (20 Points)

The following exercise deals with this oscillatory system:
![[../Files/Pasted image 20250628165348.png|center|800]]
[Figure 1: Two-mass spring-damper system diagram]

A colleague has taken some calculation steps off your hands and given you the following solution:

![[../Files/Pasted image 20250628165443.png|center|800]]
[Figure 2: Free body diagram showing forces]



$$
F_{c1} = c_1x_1 \quad F_{c2} = c_2(x_2 - x_1)
$$

 

$$
F_{b1} = b_1\dot{x}_1 \quad F_{b2} = -b_2\dot{x}_1
$$





$$
\sum F_{x1} = m_1\ddot{x}_1 = c_2x_2 - c_2x_1 - c_1x_1 - b_1\dot{x}_1
$$

 

$$
\sum F_{x2} = m_2\ddot{x}_2 = -b_2\dot{x}_2 - c_2x_2 + c_2x_1
$$



### Tasks:

1. Solve the system of coupled differential equations using scipy. Mass $m_2$ has an initial displacement of 5m. All other initial conditions are zero. Plot the velocity of both masses in the first 250 seconds over time. Create a figure with 2 side-by-side subplots. In the left plot, the extension of spring 2 should be displayed over time. In the right plot, the spring force of spring 2 should be displayed over time.
    
    Use the following parameters:
    
    - $c_1 = 1$ N/m; $c_2 = 0.1$ N/m; $b_1 = 0.01$ Ns/m; $b_2 = 0.05$ Ns/m; $m_1 = 3$ kg; $m_2 = 1$ kg
2. Spring $c_2$ is now replaced by the spring from Exercise 1. All other parameters of this exercise remain the same. Import the function definition from Exercise 1.2 with an appropriate import command. Create a new *.py file for this and insert the function there. Load the optimal values from the txt file saved in Exercise 1. If you could not solve Exercise 1, you can use the values [$a = 5, b = 14$]. Create all plots required in task 2.1 again.
    

---

## Exercise 3: Object-Oriented Programming (15 Points)

As a software developer for a small company, you have been commissioned to create a Digital Vaccination Passport. The digital vaccination passport should enable operators of restaurants, clubs, and shops to easily assess the health status of the holder. Vaccinated, recovered, and tested persons should be treated equally. You have already created a UML class diagram (Figure 3) for your software solution. In subtasks 1-5, you can now develop the vaccination passport in a structured manner.

### UML Class Diagram:
![[../Files/Pasted image 20250628165610.png|center|300]]
### Tasks:

1. Define the class `Impfpass`. In the magic method `__init__()`, the protected attributes `_geimpft` and `_genesen` should be initialized with the value `False`. The protected attribute `_getestet` should be initialized with the value `datetime.datetime.now() - datetime.timedelta(hours=25)`. First import the datetime module from the Python Standard Library for this.
    
2. Write the protected methods `_set_geimpft()` and `_set_genesen()`. The setter methods should set the respective associated attributes `_geimpft` and `_genesen` to the value `True`.
    
3. Now write the protected method `_set_getestet`. In the method, set the attribute `_getestet` to the value `datetime.datetime.now()`.
    
4. Now write the public method `einlass_erlaubt()`. The method should return `True` as a return value if the passport holder is either vaccinated or recovered or the last test is not more than 24 hours ago. You can define a time span of 24h via `datetime.timedelta(hours=24)`. Otherwise, the method should return `False`.
    
5. Now instantiate an object of the class `Impfpass` outside the class definition. Use the method `einlass_erlaubt()` and output the result as a complete sentence via a formatted string with the print command. Now use the method `_set_getestet()` and output the result again as a sentence.
    

---

## Exercise 4: Debugging (5 Points)

Given is the following faulty function:

```python
def crazy_function(number='7', new_list=()):
    """
    Output: bool_value: Checks if number_sum equals 41
           number_sum: Sum of list entries
           Monty: String object with content Monty
    """
    new_list.extend([number, number])
    new_list = new_list * 3
    number_sum = np.sum(new_list)
    bool_value = number_sum != 42
    return [bool_value, number_sum, Monty]
```

The function `crazy_function()` should return the tuple `(True, 42, 'Monty')` for the input parameter `number = 7`. Unfortunately, several errors have crept in.

### Tasks:

1. First check the default arguments of the function and correct them if necessary.
    
2. Correct the individual calculation steps so that no more errors are generated and the result `(True, 42, 'Monty')` is output as a tuple.
    
3. Call the function and output the result in the console.
    

---

