---
title: Error Rate comparison between a Random Guess and a Bayesian Guess
draft: false
tags:
---
**For a 4-class problem and a known feature vector $\mathbf{x}=\mathbf{O}$ you obtain the following posteriors:**

| s                   | 1   | 2    | 3   | 4    |
| ------------------- | --- | ---- | --- | ---- |
| P(s \| **x**=**0**) | 0.1 | 0.15 | 0.7 | 0.05 |

**What is the error rate, if you randomly throw the dice? What is the error rate, if you employ the Bayes classifier?**

- **Random**
$$
\begin{align}
\text{Error Rate} &= 1-\frac 1 n\\
&= 0.75
\end{align}
$$

- **[[240410 Bayes Classifier|Bayes Classifier]]** Chooses the class with the most probable [[240401 Bayes Theorem|A Posteriori]]. 
$$
\begin{align}
\text{Error Rate}&= 1 -\arg \max _{i \in \mathcal{S}} p(s=i\mid \mathbf{x}) \\
&=1 - 0.7\\
&=0.3
\end{align}
$$


 




