Status: #finished  
## Use case 
If the data is observed sequential, we can update our current predictions from the knowledge of the past predictions. 

$$
P\left(\mathbf{w} \mid D_{k+1}\right)=\frac{P\left(D_{k+1} \mid \mathbf{w}\right) P\left(\mathbf{w} \mid D_k\right)}{P\left(D_{k+1}\right)}
$$

Where, 
- $\textbf w\rightarrow$ Model Parameter to be learned. 
- $D\rightarrow$ Data

> Note: Here the posterior from the previous step becomes the prior for the current step. 


