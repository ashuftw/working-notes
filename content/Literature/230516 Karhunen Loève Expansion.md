---
title: Karhunen Loève Expansion
draft: false
date: 2023-05-16
---
## Definition

The KL expansion is a Transformation technique allows you to find a new set of variables that are uncorrelated and can describe the original data.
It does this by finding the most important patterns or modes of variation in the data and expressing the original variables as a combination of these patterns.

> Karhunen Loève Expansion is an instance of Model Order Reduction since it not only removes correlation but also allow to reduce the number of Random Variables. 

[[230606 Multivariate Gaussian PDF|Multivariate Gaussian PDF]] 

## Discrete KL Expansion

![[../Files/230726 Karhunen Loeve Expansion 1.png|center]]

## Continuous Karhunen Loève Expansion

![[../Files/Pasted image 20230731153838.png|center]]
**Truncation Error**
![[../Files/Pasted image 20230731153716.png|center]]
## Flashcards
**What is the primary purpose of the Karhunen-Loève (KL) expansion in the context of uncertainty quantification?**

The KL expansion is used to transform a vector of **correlated** random variables into a new set of **uncorrelated** random variables. This is a crucial preprocessing step, as many UQ methods, like Polynomial Chaos or certain quadrature rules, are designed to work with independent or uncorrelated inputs.

---

**How does the KL expansion help reduce the dimensionality of an uncertainty problem?**

The KL expansion is a model order reduction technique. The expansion is a series where each term's importance is weighted by an eigenvalue ($\lambda_i$) of the covariance matrix. Since the eigenvalues often decay rapidly, the series can be **truncated** by keeping only the terms with the largest eigenvalues. This effectively reduces the number of random variables needed to represent the system's uncertainty without losing significant information.

---

**How is the KL expansion used to handle uncertainty in distributed parameters, like random fields or processes?**

A random field (e.g., a material property varying in space) is technically infinite-dimensional. The KL expansion provides a way to **discretize** the field by representing it as a finite, truncated sum. Each term in the sum consists of a deterministic spatial function (an eigenfunction) multiplied by a single uncorrelated random variable. This converts the infinite-dimensional problem into a tractable one with a finite number of random variables.

---

### The Discrete KL Expansion Formula
**Question:** What is the mathematical formula for the truncated discrete KL expansion?
**Answer:** An uncertain random vector $X$ can be approximated by its truncated KL expansion, $X_t$, as:
$$
X_t = \mu + \sum_{l=1}^{n_t} \sqrt{\lambda_l} v_l \xi_l
$$
- $\mu$ is the mean vector of $X$.
- $\lambda_l$ and $v_l$ are the eigenvalues and eigenvectors of the covariance matrix of $X$.
- $\xi_l$ are the new, uncorrelated random variables (typically standard normal).
- $n_t$ is the number of terms after truncation.