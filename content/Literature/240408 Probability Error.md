---
title: Probability Error
draft: false
tags:
---
  
## Two Class Problem 

$$
\begin{aligned}
P(\text { error } \mid \mathbf{x}) & =\min [P(s=1 \mid \mathbf{x}), P(s=2 \mid \mathbf{x})] \\
& =1-\max [P(s=1 \mid \mathbf{x}), P(s=2 \mid \mathbf{x}))]
\end{aligned}
$$

## Multi-class Problem

$$
P^*=P( \text{error} \mid \mathbf{x})=1-\max _{i \in S}[\overbrace{P(s=i \mid \mathbf{x})}^\text{a posteriori}]
$$

Gives the Lowest Error Probability. 

### Why Doesn't the generalisation $\min [P(s=i \mid \mathbf{x})]$ work?

**The actual chance of an error is bounded by how likely it is that our best guess is wrong.** 
*Example:*
- $P(s=1 \mid x)=0.7$ (Class 1 has a $70 \%$ chance)
- $P(s=2 \mid x)=0.2$ (Class 2 has a $20 \%$ chance)
- $P(s=3 \mid x)=0.1$ (Class 3 has a 10\% chance)
Using this approach, 
$$
P(\operatorname{error} \mid x)=\min [0.7,0.2,0.1]=0.1
$$

However, the actual chance of an error is bounded by how likely it is that our best guess is wrong i.e $s=1$

$$
P( \text{error} \mid x)=1-\max [0.7,0.2,0.1]=1-0.7=0.3
$$

$\therefore$ The Lowest Probability Error is actually $30\%$

 > Note: In the two case problem, the situation is binary i.e. the least likely error corresponds to the best guess automatically making the other case the worst guess. 
