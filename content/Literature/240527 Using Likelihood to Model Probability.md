Status: #finished 

![[Pasted image 20240527153253.png|center|500]]
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
For a given parametric model $y(x, \mathbf{w})$ and target $t$. The noise can modelled by the Gaussian Distribution $\mathcal{N}$.

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
We define the Likelihood function (**Data-Likelihood**) and express it as a [[230712 Joint Density|joint density function]] where the stochasity at each target value is expressed through the Gaussian. 

$$
\boxed{
L(\mathbf{w})  =P(T \mid X, \mathbf{w}, \beta) =\prod_{n=1}^N \mathcal{N}\left(t_n \mid y\left(x_n \mathbf{w}\right), \beta^{-1}\right)
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
Use the parameters $\mathbf{w}_{ML}$ & $\beta_{ML}$ then the optimal output distribution is Gaussian: 
$$
p(t \mid x, \mathbf{w}_{ML}, \beta_{ML}) = \mathcal{N}(t \mid y(x, \mathbf{w}_{ML}), \beta_{ML}^{-1})
$$

![[Pasted image 20240603130627.png|center|500]]

[^1]: Pattern Recognition Bishop Pg. 29 