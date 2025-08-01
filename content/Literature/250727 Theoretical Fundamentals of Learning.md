---
title: Theoretical Fundamentals of Learning
draft: false
tags: 
date:
---
## 1. Notion Pairs Explained

#### Supervised vs. Unsupervised Learning
- In **supervised learning**, the goal is to find a function that maps inputs to given outputs using labeled data pairs.
- **Unsupervised learning** works with unlabeled data to find patterns or model the underlying data distribution.

#### Batch vs. Incremental Learning	
- **Batch learning** uses the entire dataset at once to perform a training update. 
- **Incremental learning** processes data points one by one, updating the model sequentially after each point.
#### Offline vs. Online Learning
- **Offline learning** refers to training that is done before a model is deployed, which can be done in either batch or incremental mode.
- **Online learning** happens at runtime as new data arrives and is therefore always incremental.

#### Error/Cost vs. Likelihood
These concepts are inversely related. Minimizing an error or cost function is often equivalent to maximizing a likelihood function. The error function can be defined as the negative log-likelihood of the data given the model's parameters.
#### Empirical vs. True Error
- The **empirical error** is calculated on the finite training dataset you have. 
- The **true error** is the error the model would make on the entire, infinite distribution of data, which is what we actually want to minimize. The empirical error for the learned parameters is typically lower than the true error because the model tends to overfit the training data.

---
## 2. Example of a Cost Function

A common cost function in supervised learning is the **sum-of-squared errors** with a regularization term, which penalizes model complexity:
$$E(w)=\frac{1}{2}\sum_{n=1}^{N}(t_{n}-w^{T}\phi(x_{n}))^{2}+\frac{\lambda}{2}||w||^{2}$$

---
## 3. Generalization Ability

The **generalization ability** (or capability) of a model is a measure of how well it performs on new, unseen data after being trained on a finite dataset. It's quantified by the difference between the true error and the empirical error. A model with good generalization ability does not just memorize the training data but captures the underlying patterns.

---
## 4. Model Complexity and Overfitting

Model complexity and overfitting are directly related:
* **Underfitting**: A model with too little complexity can't capture the underlying trend in the data, resulting in high error on both training and test sets.
* **Overfitting**: As a model's complexity increases, it can fit the training data so well that it begins to learn the noise rather than the signal. This results in very low training error but high error on new data (poor generalization).
* **Optimal Complexity**: There is typically a sweet spot of "optimal model complexity" that minimizes the true error, balancing the trade-off between underfitting and overfitting.

---
## 5. Cross-Validation

**Cross-validation** is a technique for assessing how the results of a statistical analysis will generalize to an independent data set. It's used to get a better estimate of the true error when you only have a finite amount of data.

---
## 6. Noise in Learning

Noise can have both negative and positive effects on learning:

* **How Noise Disturbs Learning**:
    * Noise in the **output** data (aleatoric uncertainty) sets a lower bound on the generalization error; a model cannot be more accurate than the inherent noise in the data.
    * A complex model can easily **overfit** by learning the noise in the training data instead of the true relationship, which hurts its performance on new data.

* **How Noise Helps Learning**:
    * Intentionally adding noise to the **input** data can act as a form of **data augmentation**. This creates more training examples and can make the model more robust, effectively reducing the generalization error.