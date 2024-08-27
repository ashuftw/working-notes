  
### Bias
In a model, it is the systematic error that is cause due to wrong assumptions made during the learning process. 

$$
\text{Bias}_D(\hat Y)= E[\hat Y]- Y
$$


### Variance
It is the measure of the deviation of the data from it's [[230509 Moment of a Random Variable|mean position]]. 

$$
\text{Var}_D(\hat Y) = E[(E[\hat Y]- \hat Y )^2]
$$

where, 
- $\hat Y\rightarrow$ Predicted target value 
- $Y\rightarrow$ Actual target value
- $D\rightarrow$ Dataset

![[Pasted image 20240710153658.png|center|500]]


## Reducing Bias 
- Increase model complexity / Parameters. 
- May cause over-fitting. 
## Reducing Variance 
- Cross validation. 
- Feature selection (selecting only necessary features reduces model complexity and variance error). 
- Regularization. 

