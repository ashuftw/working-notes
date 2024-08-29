  

## Use-case
It is used to find the smallest cost function for a regression. So that the regression gives a fairly accurate approximation of the data set. 

$$
\boxed{
\theta_j:=\theta_j-\alpha \frac{\partial}{\partial \theta_j} J\left(\theta_0, \theta_1\right) \text { (for } j=0, j=1 \text { )} }
$$

## Theory
**Hypothesis Function**

$$
h_\theta(x)=\theta_1x + \theta_0
$$

Where, 
- $(\theta_0, \theta_1)\rightarrow$ Parameters guessed by the Hypothesis function through regression
- $x\rightarrow$ Domain


## Example
![[Pasted image 20231205145446.png|center]]
**Cost/Loss Function: Mean Squared Error**

$$
J\left(\theta_0, \theta_1\right)=\frac{1}{m} \sum_{i=1}^m\left[h_\theta\left(x(i)-y(i)\right)^2\right]
$$

Where, $m\rightarrow$ Number of data points. 

The cost function is computed for all the guess values can be visualized as follows. Visually, the point with the lowest cost function can be identified. However, it is not feasible to map the cost function to every possible guess value of $\theta_1, \theta_0$. 
![[Pasted image 20231113101952.png|400]]
**Gradient algorithm** is then used to find a path to *a* minima of the cost function. 

$$
\theta_j:=\theta_j-{\alpha} \frac{\partial}{\partial \theta_j} J\left(\theta_0, \theta_1\right) \text { (for } j=0, j=1 \text { ) }
$$

This gives the smallest value of $\theta_j$ for a given $\alpha$ because we know that the [[231205 Gradient Points to the direction of Steepest Slope|gradient points to the direction of the steepest slope.]] 
Where $\alpha\rightarrow$ step size $\rightarrow$ learning rate 

$$
\begin{aligned}
& \theta_0:=\theta_0+\nabla \theta_0 \rightarrow-\alpha \frac{\partial}{\partial \theta_0} J\left(\theta_0, \theta_1\right) \\
& \theta_1:=\theta_1+\nabla \theta_1 \rightarrow-\alpha \frac{\partial}{\partial \theta_1} J\left(\theta_0, \theta_1\right)
\end{aligned}
$$

*Repeat until convergence*
