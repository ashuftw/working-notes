---
title: Discriminant Function (Multi-category)
draft: true
tags: 
date: 2025-08-14
---
## General structure of a statistical Pattern Classifier

![[../Files/Pasted image 20250814160200.png|center|500]]

- A general statistical pattern classifier takes a $d-$dimensional feature vector, $\mathbf x$, as input. 
- This vector is fed into a set of **N** (or **A**) discriminant functions, one for each class (or action).
- Each function, $g_i(x)$, computes a score for its corresponding class. 
- Finally, a decision rule, typically an **arg max()** operation, selects the class $s^*$ (or action $a^*$) that corresponds to the discriminant function with the highest score.

## **Minimum-Error-Rate Case**
To minimize the probability of misclassification, the discriminant function is set to be the posterior probability for each class, $g_i(x) = P(s=i|x)$. The decision rule $\arg\max_i g_i(x)$ then directly implements the Maximum A Posteriori (MAP) rule.
## **General Case with Risks**
When different classification errors have different costs, the goal is to minimize the overall risk. In this case, the discriminant function is defined as the negative of the conditional risk, $g_i(x) = -R(a=i|x)$. The $\arg\max$ operation on $g_i(x)$ is then equivalent to choosing the action that minimizes the risk.
