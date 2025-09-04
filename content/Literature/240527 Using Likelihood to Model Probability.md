---
title: Using Likelihood to Model Probability
draft: false
date: 2024-05-27
---

![[../Files/Pasted image 20240527153253.png|center|500]]

## Likelihood function

The likelihood function measures how likely it to observe an output for a give set of parameters to a model. 
**Mathematically** it is represented through the conditional probability. 



$$
p(t_0 | x_0, w, β)
$$



where, 
- $p\rightarrow$ PDF 
- $t_0\rightarrow$  an output
- $x_0\rightarrow$ an input
- $\text  w\rightarrow$ model parameter. Example: In a linear regression model relating $x$ and $t$ 





	$$
	t\approx P(x)=w_0+w_1 x
	$$





Here, $\mathbf{w}=\left[w_0, w_1\right]$ are the parameters of the model. $w_0$ is the intercept, and $w_1$ is the slope.
- $β\rightarrow$ precision, is the inverse of the variance ($σ^2$).  
*Note: High precision means low variance and vice versa.*

## Assumption 

The probability is assumed to be Gaussian distributed with mean on the model and variance $β^{-1} = σ^2$ (for the 1-dimensional case)[^1]



$$
p(t_0 | x_0, w, β) = \mathcal N(t_0 | y(w, x_0), \beta^{-1})
$$



where, 
- $y\rightarrow$ is the regression model used. 

## Measurement to Stochastic Model

For a given parametric model $y(x, \mathbf{w})$ and target $t$. The noise can be modeled by the Gaussian Distribution $\mathcal{N}$.



$$
t=y(x, \mathbf{w})+\mathcal{N}\left(0, \beta^{-1}\right)
$$



The Mean is $0$ because we center the Gaussian around the predicted value.

Since we have a distribution (Probabilistic), the equality is removed.



$$
t-y(x, \mathbf{w}) \sim \mathcal{N}\left(0, \beta^{-1}\right)
$$



Finally we get



$$
\boxed{
t \sim \mathcal{N}\left(y(x, \mathbf{w}), \beta^{-1}\right)
}
$$



## Applying this to the  whole Data-set

We define the Likelihood function (**Data-Likelihood**) and express it as a [[230712 Joint Density|joint density function]] where the stochasticity at each target value is expressed through the Gaussian. 



$$
\boxed{
L(\mathbf{w})  =P(T \mid X, \mathbf{w}, \beta) =\prod_{n=1}^N \mathcal{N}\left(t_n \mid y\left(x_n ,\mathbf{w}\right), \beta^{-1}\right)
}
$$



Note: 
- We assume the data points to be independent. *Inductive bias!*
- The Joint Density of a Independent values is the product of the densities of individual data. 

## Parameter Optimisation

Involves maximising the Likelihood for the given parameters i.e. we maximise the probability of observing the measured output ($t$) for a given model parameter ($\text w$) and input ($x$)



$$
\omega_{ML} = \omega^* = \arg\max _\omega L(\omega)
$$



> Note: the actual value of  $L(\mathbf{w})$ at the maximum is not important!

## Generalisation 

Select parameters $\mathbf{w}_{ML}$ & $\beta_{ML}$ which maximize the likelihood and  represent the optimal output distribution as a Gaussian: 



$$
p(t \mid x, \mathbf{w}_{ML}, \beta_{ML}) = \mathcal{N}(t \mid y(x, \mathbf{w}_{ML}), \beta_{ML}^{-1})
$$



![[../Files/Pasted image 20240603130627.png|center|500]]

### Finding parameters from the probabilistic approach

- Start with the stochastic data model:





	$$
	t = y(x, w) + \nu
	$$





where $\nu \sim \mathcal{N}(0, \beta^{-1})$
- Construct the likelihood function for a single data point:





	$$
	p(t_n | x_n, w, \beta) = \mathcal{N}(t_n | y(x_n, w), \beta^{-1})
	$$





- Form the data likelihood by assuming independence of data points:





	$$
	p(\mathbf{t} | \mathbf{X}, w, \beta) = \prod_{i=1}^{N} \mathcal{N}(t_i | y(x_i, w), \beta^{-1})
	$$





- Take the negative logarithm to get the error function:





	$$
	E(w) = -\ln p(\mathbf{t} | \mathbf{X}, w, \beta) = \frac{\beta}{2}\sum_{i=1}^{N}(t_i - y(x_i, w))^2 + \frac{N}{2}\ln\frac{2\pi}{\beta}
	$$





5) Minimize $E(w)$ by setting its derivative to zero:
   $\nabla E(w) = -\beta\sum_{i=1}^{N}(t_i - y(x_i, w))\nabla y(x_i, w) = 0$

6) For linear models $y(x, w) = w^T \Phi(x)$, this gives:
   $w_{ML} = (\Phi^T \Phi)^{-1}\Phi^T \mathbf{t}$

7) The optimal precision parameter is:
   $\beta_{ML} = \frac{N}{\sum_{i=1}^{N}(t_i - y(x_i, w_{ML}))^2}$

[^1]: Pattern Recognition Bishop Pg. 29 