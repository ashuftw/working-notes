---
title: Bayesian Discriminant Function
draft: false
date: 2024-04-23
---
The Bayesian (minimum error rate) discriminant function $g(\mathbf{x})$ is a decision rule that selects the class with the highest posterior probability given a feature vector $\mathbf{x}$ :



$$
g(\mathbf{x})=\arg \max _i P(s=i \mid \mathbf{x})
$$



In contrast, $g_i(\mathbf{x})$ is the discriminant function for a specific class $i$, which calculates a score for that class:



$$
g_i(\mathbf{x})=P(s=i \mid \mathbf{x})
$$



Classification is performed by computing $g_i(\mathbf{x})$ for each class and selecting the class with the highest value. This approach minimizes the overall probability of classification error.

---

### Class Problems



$$
\boxed{s^*=\arg \max _{i \in \mathcal{S}} g_i(\mathbf x)}
$$



where, $g_i(\mathbf{x}) = P(s = i|\mathbf{x})$, gives the **minimum error rate classification.**

### Decision Problems



$$
\boxed{a^*=\arg \max _{j \in \mathcal{A}} g_i(\mathbf x)}
$$



where, $g_i(\mathbf{x}) = -R(a = i|\mathbf{x})$, gives the **minimum risk decision.** 

