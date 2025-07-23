---
title: Logistic Regression (Probabilistic Discriminative Model)
draft: false
tags: 
date: 2025-07-14
---
Here, the [[240401 Posterior, Likelihood, Prior and Evidence|Posterior]] is modeled directly as a function of $x$. The posterior probability is specified using a sigmoid function applied to a linear function of the input ([[250714 Logistic Regression (Probabilistic Discriminative Model)|Logistic Regression]])

$$
p(C_k|x_n) = y(x_n) = \sigma(w^T x_n)
$$

where, 
- $y(x_n​)\rightarrow$ This is the Model Prediction.
- $\sigma\rightarrow$ [[250714 Sigmoid Function|Sigmoid Function]] that squashes it's input values into a value between $0$ and $1$
- $w^Tx_n​\rightarrow$ Linear Model 
