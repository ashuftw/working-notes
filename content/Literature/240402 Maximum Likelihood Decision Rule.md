---
title: Maximum Likelihood Decision Rule
draft: false
tags: []
---
## Definition 
It gives the formula to find the most like state for a given evidence.  


$$
s^*=\arg \max _{i \in \mathcal{S}} \underbrace{p(\mathbf{x} \mid s=i)}_{\text{Likelihood}}
$$

where, 
- $s^*$: Class that maximizes the **Likelihood** function.
- $\mathbf x$: feature vector
- $s$: Class

**Note**
- When there no Prior i.e. $P(s=i)=1$, the classes are equiprobable, i.e. $P(s=i)=\frac{1}{N}$, then the [[240410 Bayes Classifier|Bayes Classifier]] becomes a [[240402 Maximum Likelihood Decision Rule|Maximum Likelihood Decision Rule]].
- The act of choosing the state to find the highest Likelihood is the *decision* here. 





---
# References
