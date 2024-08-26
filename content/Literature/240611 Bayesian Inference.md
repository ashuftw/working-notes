Status: #finished  
## Use case
It is used to calculate the model parameters $\textbf w$ from the data.  **The a-Posteriori is given as the product of the Likelihood and the Prior.**


$$
p(\mathbf{w}|\mathbf{x}, \mathbf{t}, \alpha, \beta) \propto p(\mathbf{t}|\mathbf{x}, \mathbf{w}, \beta) p(\mathbf{w}|\alpha)
$$

where,
- $\textbf w\rightarrow$ Model parameter that has to be learned (for example weights.)
- $\textbf x\rightarrow$ Input vector
- $\textbf t\rightarrow$ Target 
- $β\rightarrow$ Precision, is the inverse of the variance ($σ^2$).  It measures how tightly the data is clustered along the weights. 
- $\alpha\rightarrow$ Hyper-parameter that is independent of the data Ex: Learning rate, batch size, regularization parameters etc. 


---
# References
