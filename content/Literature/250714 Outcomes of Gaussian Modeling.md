---
title: Outcomes of Gaussian Modeling
draft: false
tags: 
date: 2025-07-14
---
The shape of the decision boundary is determined by whether the Gaussian "shapes" used to model the classes are identical or not. The final classification decision is then typically made by choosing the class with the highest probability for a given input.

When classes are modeled with Gaussian functions, the result depends on the covariance matrices of those functions.
### **Linear Decision Boundary**
If the Gaussian distributions for the different classes share the same covariance matrix ( $\boldsymbol{\Sigma}$ ), the resulting decision boundary between them will be linear. This outcome is equivalent to Fisher's linear discriminant.
#### **Non-Linear Decision Boundary**
If the classes have different covariance matrices, the decision boundary becomes non-linear.

