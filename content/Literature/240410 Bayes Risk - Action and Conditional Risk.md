---
title: Bayes Risk - Action and Conditional Risk
draft: false
tags: []
---
## Conditional Risk
The Risk associated with taking a decision $a$ given the observation $\mathbf x$ or simply the cost of a decision is given by,
$$\boxed{
R(a=j \mid \mathbf{x})=\sum_{i \in \mathcal{S}} \overbrace{\lambda(a=j \mid s=i)}^{cost} \underbrace{P(s=i \mid \mathbf{x})}_{Posteriori}
}$$
where, 
- $a \in \mathcal{A}=\{1,2, \ldots, A\}$ represents the action 
- $\lambda$ is the loss function, such that $\lambda(a=j \mid s=i)$ states how costly an action $a=j$ given a classification $s  = i$

> Note: The Cost function is entered manually. So that the decision that would lead to a negative outcome is weighted with a very high cost. 

## **Example**
Consider a Two Class problem such that
1. **Actions** $a\in A =\{\text{Treat}, \text{Don't Treat} \}$ 
2. **Classification** $s\in S=\{\text{Sick},\text{Healthy}\}$
 **Loss function** 
- $\lambda( a=1\mid s= 1)$ : Low
- $\lambda( a=1\mid s= 2)$ : High 
- $\lambda( a=2\mid s= 1)$ : High 
- $\lambda( a=2\mid s= 2)$ : Low

Give that we use a Bayes Classifier to make diagnosis a on the Patient. The *Conditional Risk* can be calculated as follows. 
$$\begin{align}
R(1\mid \mathbf{x})=\lambda( 1  \mid s=1)\cdot P(s=1 \mid \mathbf{x})+\lambda( 1  \mid s=2) \cdot P(s=2 \mid \mathbf{x})
\\
R( 2 \mid \mathbf{x})=\lambda( 2 \mid s=1)\cdot  P(s=1 \mid \mathbf{x})+\lambda( 2  \mid s=2) \cdot P(s=2 \mid \mathbf{x})
\end{align}$$
## Bayes Decision Rule for Actions
$$\boxed{
a^*=\arg \min _{j \in \mathcal{A}} R(a=j \mid \mathbf{x})
}$$

Thus the best action would be the one that minimizes the risk. 

---
# References
