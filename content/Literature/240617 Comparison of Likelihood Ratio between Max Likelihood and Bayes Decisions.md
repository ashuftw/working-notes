Status: #finished 

### [[240423 Likelihood Ratio|Likelihood Ratio]] for Binary Classification
$$\boxed{ LR(\mathbf{x}) = \frac{p(\mathbf{x}|s = 1)}{p(\mathbf{x}|s = 2)} > \theta \Rightarrow \text{Decide for } s = 1, \text{ else for } s = 2. 
}$$
## Variants of the threshold:
- **Maximum Likelihood Decision** 
	$$\theta = 1$$
	Here if the probability $p(\textbf x|s=1)$ greater than the denominator. The threshold has to be greater than one. This is same as choosing making a classification based on which classification has a higher probability. 
- **Bayes Decision**  
	$$\theta = \dfrac{P(s = 2)}{P(s = 1)}$$
	Here we make use of the Priors. Thus if we already know that a particular classification is more probable, we can use this knowledge to essentially weight the threshold $\theta$. 
	
	*Note: Since we define $LR$ to be greater than $\theta$, you want it to be smaller for a preferable classification, hence the ratio is flipped.* 






---
# References
