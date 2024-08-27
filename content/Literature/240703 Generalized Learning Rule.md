Status: #finished 
![[Pasted image 20240703122006.png|center|500]]

Using the Gradient Descent Method the **Generalized Learning Rule** can be obtained as 

$$
\boxed{
\mathbf{w}_{k+1}=\mathbf{w}_k-\eta \nabla E(\mathbf{w})
}
$$

where, 
- $\textbf{w}_{k+1}\rightarrow$Model Weight (Learned)
- $\eta\rightarrow$Learning Rate is step size taken during each iteration of the Gradient descent 
- $E(\mathbf{w})\rightarrow$Error Function
$$
E(\mathbf{w})=\frac{1}{2 N} \sum_{n=1}^N\left(y\left(x_n, \mathbf{w}\right)-t_n\right)^2 \quad + \underbrace{\lambda||\textbf w||^2}_\text{ (regularization)}
$$

- The initial position is random or a good guess is taken. 
- Iteration is run until $E(\textbf w)\approx 0$ 

