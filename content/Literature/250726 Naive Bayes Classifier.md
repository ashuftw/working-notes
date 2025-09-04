---
title: Naive Bayes Classifier
draft: false
tags: 
date: 2025-07-26
---
The **Naive Bayes classifier** is a probabilistic classifier that applies Bayes' theorem with a strong ("naive") assumption of conditional independence among the features (attributes).

It calculates the probability of each possible class given the observed attribute values and selects the class with the highest posterior probability.

The classifier is defined by the formula:

$$
\hat{c} = \underset{c_k}{\mathrm{argmax}} \, P(c_k) \prod_{n=1}^{N} P(x_n | c_k)
$$

where $\hat{c}$ is the predicted class, $c_k$ is a possible class, and $x_n$ are the attribute values of the instance to be classified.
> ***Note: Naive Bayes Classifier uses attributes directly instead of hypotheses!***

The terms are estimated from the training data as follows:
* **Class Prior ($P(c_k)$):** This is estimated by the frequency of class $c_k$ in the dataset.  It is the number of training instances in class $c_k$ divided by the total number of training instances.
* **Attribute Likelihood ($P(x_n | c_k)$):** This is estimated by counting the frequency of attribute value $x_n$ among only those instances that belong to class $c_k$.  It is the number of instances in class $c_k$ with attribute value $x_n$, divided by the total number of instances in class $c_k$.