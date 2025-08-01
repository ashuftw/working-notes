---
title: Numerical Methods - Practice Test
draft: false
tags: 
date: 2025-06-23
---

## Task 1 
![[../Files/Pasted image 20250623173357.png]]
### Solution
![[../Files/IMG_20250623_184629360.jpg]]

Constant means the degree is $0$
## Task 2 
![[../Files/Pasted image 20250624104927.png]]
### Solution 
[[230507 Quadrature - Derivation and Formulae]]
**Quadrature error estimation**
- $f^{\prime \prime}(x)=12 c_1 x^2+6 c_2 x=-x^2+2 x$
- Check: $f^{\prime \prime}(-1)=-3, f^{\prime \prime}(1)=1, f^{\prime \prime}(3)=-3$
- Therefore $M_2=3$

**Error bound (in formulary)** 

$$
|R(f)| \leq \frac{(b-a)^3}{12} M_2
$$



$$
|R(f)| \leq \frac{(3-(-1))^3}{12} \cdot 3=\frac{64}{12} \cdot 3=16
$$


For $c_1=c_2=0, c_3, c_4 \in \mathbb{R}$ :
$f(x)=c_3 x+c_4$ is a polynomial of degree $1$ .

Since the trapezoid rule has degree of accuracy 1, it integrates all polynomials of degree $\leq 1$ exactly.

Therefore, the quadrature error is exactly 0 .


**Exam relevance**: Error estimation formulas are frequently tested!
## Task 3 
![[../Files/Pasted image 20250624123835.png]]
### Solution
#### Part (a) - Romberg Extrapolation for Forward Difference Quotient

The forward difference quotient has the form: 

$$
f'(x) \approx \frac{f(x+h) - f(x)}{h}
$$


From Taylor expansion: 

$$
f(x+h) = f(x) + hf'(x) + \frac{h^2}{2}f''(x) + O(h^3)
$$

Rearranging, we have 

$$
\frac{f(x+h) - f(x)}{h} = f'(x) + \overbrace{\frac{h}{2}f''(x) + O(h^2)}^{O(h)}
$$


This shows the forward difference quotient has **convergence order** **1**.
**Applying Romberg extrapolation**
Let $A(h) = \frac{f(x+h) - f(x)}{h}$ and $\frac{f^{\prime \prime}(x)}{2} = c$

Then we have 

$$
A(h) = f'(x) + ch + O(h^2)
$$

- $A(h) = f'(x) + ch + O(h^2)$
- $A(h/2) = f'(x) + c\frac{h}{2} + O(h^2)$

Using Romberg's formula with $q = 1$: 

$$
A_{new} = \frac{2A(h/2) - A(h)}{2-1} = 2A(h/2) - A(h)= f'(x)+O(h^2)
$$


 **Convergence order 2**.

Substituting to get the calculation formula: 


$$
Q_{new} = 2 \cdot \frac{f(x+h/2) - f(x)}{h/2} - \frac{f(x+h) - f(x)}{h}
$$

 


$$
= \frac{-3f(x) + 4f(x+h/2) - f(x+h)}{h}
$$

##### **Common Mistakes**
***Why do we consider the full Taylor Polynomial?***
Because is acts as the Blueprint for the error. Note that in Romberg extrapolation is  basically a clever trick to cancel out the errors.  
***Why expand up to $f''$ and not directly use the $O(h)$ notation?***
Same answer as above: We need the term so that we can cancel it out! 


#### Part (b) - Numerical Approximations

For $f(x) = x^{-1}$ at $x = 1$ with $h = 1/2$:
- $f(1) = 1$
- $f(3/2) = 2/3$
- $f(1/2) = 2$

**Exact derivative:** $f'(x) = -x^{-2}$, so $f'(1) = -1$

**Forward difference quotient:** 


$$
f'(1) \approx \frac{f(3/2) - f(1)}{1/2} = -\frac{2}{3}
$$



**Romberg scheme from (a):** 


$$
f'(1) \approx \frac{-3f(1) + 4f(5/4) - f(3/2)}{1/2} =-\frac{14}{15}
$$


**Central difference quotient:** 

$$
f'(1) \approx \frac{f(3/2) - f(1/2)}{2 \cdot 1/2}  = -\frac{4}{3}
$$


**Comparison with exact value $f'(1) = -1$:**
- Forward difference: $-2/3$ (error = $1/3$)
- Romberg scheme: $-14/15$ (error = $1/15$)
- Central difference: $-4/3$ (error = $1/3$)

The Romberg scheme provides the best approximation, as expected from its higher convergence order.
## Task 4 (Nonlinear Equations)
![[../Files/Pasted image 20250624133133.png]]
**Note: Newton's method formulas are available in the formulary.**
#### Part a) Derive Newton's method from Taylor expansion (1 point)

Taylor expansion of $f(x)$ around point $x_k$:


$$
f(x) = f(x_k) + f'(x_k)(x - x_k) + O((x - x_k)^2)
$$




$$
f(x) \approx f(x_k) + f^\prime(x_k)(x - x_k)
$$


To find the zero, we set this linear approximation equal to zero: 


$$
0 = f(x_k) + f^\prime(x_k)(x - x_k)
$$


Solving for $x$ gives us the next iterate: 


$$
x = x_k - \frac{f(x_k)}{f^\prime(x_k)}
$$



Therefore, **Newton's method** is: 


$$
\boxed{
x_{k+1} = x_k - \frac{f(x_k)}{f'(x_k)}}
$$


#### Part b) Calculate two Newton steps (2 points)
For $f(x) = \frac{1}{4}x^2$, we have $f'(x) =\frac{1}{2}x$
Starting from $x_0 = 4$:


$$
x_1 = x_0 - \frac{f(x_0)}{f'(x_0)} =  2
$$




$$
x_2 = x_1 - \frac{f(x_1)}{f'(x_1)} = 1
$$



**Explanation**: Newton's method approximates $f$ by its tangent line at each iteration and finds where the tangent intersects the $x-$axis.
![[../Files/Figure_1.png|center|600]]
Sketch should show parabola $f(x) = \frac{1}{4}x^2$, starting point $(4,4)$, tangent line at $x=4$ intersecting $x-$axis at $x=2$, then tangent at $x=2$ intersecting at $x=1$
#### Part c) Connection to Banach iteration and convergence order (2 points)

- [[250626 Relationship between Fixed Point Iteration & Newton's Method|Connection between Fixed Point Iteration & Newton's Method]]
- **Convergence order:** The derivative of the iteration function is:



	$$
	g'(x) = 1 - \frac{f'(x)^2 - f(x)f''(x)}{[f'(x)]^2} = \frac{f(x)f''(x)}{[f'(x)]^2}
	$$




At the root $x*$ where $f(x*) = 0$: 


$$
g'(x*) = \frac{f(x*)f''(x*)}{[f'(x*)]^2} = 0
$$



Since $g'(x*) = 0$, Newton's method has **quadratic convergence (order 2)** near the root, assuming $f'(x*)\ne 0$ and $f''(x*)$ exists.

This means the error approximately squares in each iteration: $|x_{k+1} - x*| ≈ C|x_k - x*|^2$ for some constant $C$


## Task 5 
![[../Files/Pasted image 20250723162119.png]]
### Solution
#### a) Maximal Step Size and System Property

The **Explicit Euler method** is stable if for all eigenvalues $\lambda$, the step size $h$ satisfies the condition:

$$
\boxed{
|1 + h\lambda| \le 1
}
$$
The matrix is upper triangular, the eigenvalues are its diagonal entries:

$$
\lambda_1 = -2 \quad \text{and} \quad \lambda_2 = -2
$$

Since our eigenvalues are real and identical, we only need to solve for $\lambda = -2$:

$$
|1 - 2h| \le 1
$$
This inequality can be split into two parts:
$$
(1 - 2h) \le 1\quad \text{or} \quad
(1 - 2h) \ge -1
$$
Simplifying


$$
-1 \le 1 - 2h \le 1
$$
> ***Shorthand:Any time you multiply a negative value, the inequalities flip directions.*** 
Solving for $h$:

$$
-2 \le -2h \le 0 \implies 1 \ge h \ge 0
$$

The **maximal step size is $h_{max} = 1$**.

A property of this system is that it is **not stiff**. A system is considered stiff if the ratio of the largest to the smallest absolute value of the real parts of the eigenvalues is large. Here, the ratio is $|-2|/|-2| = 1$, which is the opposite of stiff.

#### b) Two Steps with h = 0.5

The explicit Euler method is given by the formula:

$$
y_{i+1} = y_i + h_i f(t_i, y_i)
$$


$$
q_{i+1} = q_i + h A q_i
$$

Given $q_0 = \begin{pmatrix} 1 \\ 4 \end{pmatrix}$, $h=0.5$, and $A = \begin{pmatrix} -2 & -1 \\ 0 & -2 \end{pmatrix}$.

**Step 1: Calculate $q_1$**
First, we calculate the product $A q_0$:

$$
A q_0 = \begin{pmatrix} -2 & -1 \\ 0 & -2 \end{pmatrix} \begin{pmatrix} 1 \\ 4 \end{pmatrix}  = \begin{pmatrix} -6 \\ -8 \end{pmatrix}
$$

Now we find $q_1$:

$$
q_1 = q_0 + h A q_0 = \begin{pmatrix} 1 \\ 4 \end{pmatrix} + 0.5 \begin{pmatrix} -6 \\ -8 \end{pmatrix} = \begin{pmatrix} -2 \\ 0 \end{pmatrix}
$$


**Step 2: Calculate $q_2$**
First, we calculate the product $A q_1$:

$$
A q_1 = \begin{pmatrix} -2 & -1 \\ 0 & -2 \end{pmatrix} \begin{pmatrix} -2 \\ 0 \end{pmatrix} = \begin{pmatrix} 4 \\ 0 \end{pmatrix}
$$

Now we find $q_2$:

$$
q_2 = q_1 + h A q_1 = \begin{pmatrix} -2 \\ 0 \end{pmatrix} + 0.5 \begin{pmatrix} 4 \\ 0 \end{pmatrix}= \begin{pmatrix} 0 \\ 0 \end{pmatrix}
$$

After two steps, the solution is $q_2 = \begin{pmatrix} 0 \\ 0 \end{pmatrix}$.

## Task 5B
Consider differential equation:

$$
\dot{q}(t) = - \begin{pmatrix} 2 & 1 \\ 0 & 2 \end{pmatrix} q(t), \quad q(0) = \begin{pmatrix} 1 \\ 4 \end{pmatrix}.
$$


a) The **Crank-Nicolson method** is known to be A-stable. Explain what A-stability implies for the choice of step size $h$ when solving this particular system. Is this method a good choice for this system?

b) Perform **one step** of the Crank-Nicolson method with a step size of $h = 1.0$ to find the approximation $q_1$.
### a) A-Stability and Method Suitability

A numerical method is **A-stable** if its stability region contains the entire left half of the complex plane, $\{z \in \mathbb{C} : \text{Re}(z) \le 0\}$ . The Crank-Nicolson method is A-stable.

The eigenvalues of the system matrix are $\lambda_1 = \lambda_2 = -2$, which are on the negative real axis (i.e., in the left half-plane). Because the method is A-stable, the term $h\lambda$ will lie within the stability region for **any positive step size $h > 0$**.

This means that for the Crank-Nicolson method, there is **no upper limit on the step size $h$ imposed by stability**. The choice of $h$ can be based purely on the desired accuracy of the solution. This makes it a very robust and good choice, especially for stiff differential equations.
### b) One Step of Crank-Nicolson with h = 1.0


$$
y_{i+1} = y_i + \frac{h_i}{2}[f(t_i, y_i) + f(t_{i+1}, y_{i+1})]
$$

The Crank-Nicolson method for a system $\dot{q} = Aq$ is given by:

$$
q_{i+1} = q_i + \frac{h}{2}(Aq_i + Aq_{i+1})
$$

To solve for the unknown vector $q_{i+1}$, we must first rearrange the formula into a linear system of equations:

$$
q_{i+1} - \frac{h}{2}Aq_{i+1} = q_i + \frac{h}{2}Aq_i \implies \left(I - \frac{h}{2}A\right)q_{i+1} = \left(I + \frac{h}{2}A\right)q_i
$$

Given $h=1.0$, $A = \begin{pmatrix} -2 & -1 \\ 0 & -2 \end{pmatrix}$, and $q_0 = \begin{pmatrix} 1 \\ 4 \end{pmatrix}$.

**1. Set up the linear system:**
First, we compute the matrices on the left and right sides.
* **Left-Hand Side Matrix:**
    

	$$
	I - \frac{h}{2}A = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} - 0.5 \begin{pmatrix} -2 & -1 \\ 0 & -2 \end{pmatrix} = \begin{pmatrix} 2 & 0.5 \\ 0 & 2 \end{pmatrix}
	$$


* **Right-Hand Side Vector:**
    

	$$
	\left(I + \frac{h}{2}A\right)q_0 = \left(\begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} + 0.5 \begin{pmatrix} -2 & -1 \\ 0 & -2 \end{pmatrix}\right) \begin{pmatrix} 1 \\ 4 \end{pmatrix} = \begin{pmatrix} -2 \\ 0 \end{pmatrix}
	$$


The system to solve for $q_1$ is:

$$
\begin{pmatrix} 2 & 0.5 \\ 0 & 2 \end{pmatrix} q_1 = \begin{pmatrix} -2 \\ 0 \end{pmatrix}
$$


**2. Solve for $q_1$:**
Let $q_1 = \begin{pmatrix} x \\ y \end{pmatrix}$. We can solve the system using back substitution.
* From the second row: $2y = 0 \implies y = 0$.
* From the first row: $2x + 0.5y = -2 \implies 2x + 0 = -2 \implies x = -1$.

The solution after one step is:

$$
q_1 = \begin{pmatrix} -1 \\ 0 \end{pmatrix}
$$


## Task 5C 
Consider the differential equation:

$$
\dot{q}(t) = - \begin{pmatrix} 2 & 1 \\ 0 & 2 \end{pmatrix} q(t), \quad q(0) = \begin{pmatrix} 1 \\ 4 \end{pmatrix}.
$$


a) The **implicit Euler method** is known to be A-stable. Explain what this implies for the choice of step size $h$ when solving this system.

b) Perform **one step** of the implicit Euler method with a step size of $h = 1.0$ to find the approximation $q_1$.

### Solution

#### a) A-Stability and Method Suitability

A numerical method is **A-stable** if its stability region contains the entire left half of the complex plane, $\{z \in \mathbb{C} : \text{Re}(z) \le 0\}$. The implicit Euler method is A-stable.

The eigenvalues of the system matrix are $\lambda = -2$, which are in the left half-plane. Because the method is A-stable, the term $h\lambda$ will always lie inside the stability region for **any positive step size $h > 0$**.

This means there is **no upper limit on the step size $h$ for stability**. The choice of $h$ can be based purely on the desired accuracy of the solution, making the method very robust.

#### b) One Step of Implicit Euler with h = 1.0

$$
y_{i+1} = y_i + h_i f(t_{i+1}, y_{i+1})
$$

The implicit Euler method is given by the formula:

$$
q_{i+1} = q_i + h A q_{i+1}
$$

To solve for the unknown vector $q_{i+1}$, we must rearrange the formula into a linear system of equations:

$$
q_{i+1} - hAq_{i+1} = q_i \implies (I - hA)q_{i+1} = q_i
$$

Given $h=1.0$, $A = \begin{pmatrix} -2 & -1 \\ 0 & -2 \end{pmatrix}$, and $q_0 = \begin{pmatrix} 1 \\ 4 \end{pmatrix}$.

**1. Set up the linear system:**
First, we compute the matrix on the left-hand side:

$$
I - hA = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} - 1.0 \begin{pmatrix} -2 & -1 \\ 0 & -2 \end{pmatrix} =  \begin{pmatrix} 3 & 1 \\ 0 & 3 \end{pmatrix}
$$

The system to solve for $q_1$ is:

$$
\begin{pmatrix} 3 & 1 \\ 0 & 3 \end{pmatrix} q_1 = \begin{pmatrix} 1 \\ 4 \end{pmatrix}
$$


**2. Solve for $q_1$:**
Let $q_1 = \begin{pmatrix} x \\ y \end{pmatrix}$. We can solve the system using back substitution.
* From the second row: $3y = 4 \implies y = 4/3$.
* From the first row: $3x + y = 1 \implies 3x + 4/3 = 1 \implies 3x = -1/3 \implies x = -1/9$.

The solution after one step is:

$$
q_1 = \begin{pmatrix} -1/9 \\ 4/3 \end{pmatrix}
$$

## Task 6 
![[../Files/Pasted image 20250723175541.png]]
### a) Definition and Explanation of Consistency

The order of consistency tells us how quickly the error of a numerical method decreases as we make the step size $(h)$ smaller.

In other words for it answers the question "For an an infinitesimally small step, does the given method behave like the actual differential equation?"

This is measured with the **local truncation error**, $\tau(t,h)$, which is the error the method makes in a single step, assuming the starting point was perfectly accurate. 
$$
\tau(t, h) = \frac{y(t+h) - y(t)}{h} - \Phi(t, y(t), h)
$$

### b) [[250724 Order of Consistency of the Euler Method|Order of Consistency of the Euler Method]]
### c) [[250724 Order of Consistency of the Euler Method|Order of Consistency of the Euler-Heun Method]]
## Task 7 
![[../Files/Screenshot from 2025-07-24 14-49-34.png]]
### Solution 
#### a) Butcher Tableau
- **Nodes $c_i$**: The values in the left column are $c_1=0$, $c_2=1/3$, and $c_3=2/3$.
- **Matrix $A$**: The values in the main triangular part are $a_{21}=1/3$, $a_{31}=0$, and $a_{32}=2/3$.
- **Weights $b_i$**: The values in the bottom row are $b_1=1/4$, $b_2=0$, and $b_3=3/4$.

**Complete Calculation Scheme**

The complete calculation scheme derived from the Butcher tableau is:
$$
\begin{aligned}
q_1 &= hf(t_i, y_i) \\
q_2 &= hf\left(t_i + \frac{1}{3}h, y_i + \frac{1}{3}q_1\right) \\
q_3 &= hf\left(t_i + \frac{2}{3}h, y_i + \frac{2}{3}q_2\right) \\
y_{i+1} &= y_i + \frac{1}{4}q_1 + \frac{3}{4}q_3
\end{aligned}
$$
#### Part b) Calculation
 $f(t, y) = y - t$.
### Performing One Step (i=0)

1.  **Calculate Stage 1 ($q_1$):**
    Evaluate $f$ at the initial point $(t_0, y_0) = (0, 2)$.
    $$q_1 = h \cdot f(t_0, y_0) = 3 \cdot 2 = 6$$
2.  **Calculate Stage 2 ($q_2$):**
    The arguments for $f$ are:
    - Time: $t_0 + \frac{1}{3}h = 0 + \frac{1}{3}(3) = 1$
    - y-value: $y_0 + \frac{1}{3}q_1 = 2 + \frac{1}{3}(6) = 2 + 2 = 4$
    - $f(1, 4) = 4 - 1 = 3$.
    $$q_2 = hf\left(t_i + \frac{1}{3}h, y_i + \frac{1}{3}q_1\right)= h \cdot f(1, 4) = 3 \cdot 3 = 9$$
3.  **Calculate Stage 3 ($q_3$):**
    The arguments for $f$ are:
    - Time: $t_0 + \frac{2}{3}h = 0 + \frac{2}{3}(3) = 2$
    - y-value: $y_0 + \frac{2}{3}q_2 = 2 + \frac{2}{3}(9) = 2 + 6 = 8$
	-  $f(2, 8) = 8 - 2 = 6$.
    $$q_3 = h \cdot f(2, 8) = 3 \cdot 6 = 18$$
4.  **Calculate Final Update ($y_1$):**
    Using the calculated stages $q_1=6$ and $q_3=18$:
    $$y_1 = y_0 + \frac{1}{4}q_1 + \frac{3}{4}q_3=17$$
After one step with step size $h=3$, the approximate value is **$y_1 = 17$**.
## Task 8 
![[../Files/Pasted image 20250724153236.png]]
 We use a spatial step size of $\Delta x = 1/6$, which creates 5 interior grid points $x_j = j/6$ for $j=1, \dots, 5$. The solution at these points is approximated by the time-dependent functions $u_j(t) \approx u(t, x_j)$.

The second spatial derivative $u_{xx}$ is approximated using the **central difference formula**:
$$ u_{xx}(t, x_j) \approx \frac{u_{j-1}(t) - 2u_j(t) + u_{j+1}(t)}{(\Delta x)^2} $$
Substituting this into the PDE and applying the homogeneous Dirichlet boundary conditions ($u_0(t) = 0$ and $u_6(t) = 0$) results in a system of 5 ordinary differential equations.

This system can be written in matrix-vector form as:
$$ \mathbf{u}'(t) = \frac{a}{(\Delta x)^2} A \mathbf{u}(t) + \mathbf{f}(t) $$
With $\Delta x = 1/6$, $\frac{a}{(1/6)^2} = 36a$. The final system is:

$$
\begin{pmatrix} u''_1(t) \\ u''_2(t) \\ u''_3(t) \\ u''_4(t) \\ u''_5(t) \end{pmatrix}
= 36a
\begin{pmatrix}
-2 & 1 & 0 & 0 & 0 \\
1 & -2 & 1 & 0 & 0 \\
0 & 1 & -2 & 1 & 0 \\
0 & 0 & 1 & -2 & 1 \\
0 & 0 & 0 & 1 & -2
\end{pmatrix}
\begin{pmatrix} u_1(t) \\ u_2(t) \\ u_3(t) \\ u_4(t) \\ u_5(t) \end{pmatrix}
+
\begin{pmatrix} f(t, x_1) \\ f(t, x_2) \\ f(t, x_3) \\ f(t, x_4) \\ f(t, x_5) \end{pmatrix}
$$
The initial condition for this system is $\mathbf{u}(0) = [u_0(x_1), u_0(x_2), u_0(x_3), u_0(x_4), u_0(x_5)]^T$.