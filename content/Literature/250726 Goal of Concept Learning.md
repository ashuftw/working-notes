---
title: Goal of Concept Learning
draft: false
tags: 
date: 2025-07-26
---
The goal of concept learning is to infer a **boolean-valued function**, known as a concept, from a set of training examples that have been classified as either positive or negative instances of that concept. 

Equivalently, the goal is to identify a specific subset of items from a larger set. It is a fundamental task in supervised classification.

The learning scenario is formalized with the following components:

* **Instance Space ($X$):** The set of all possible instances or objects that can be classified.
* **Target Concept ($c$):** The specific function to be learned. It is a subset of the instance space ($c \subseteq X$) and can be represented as an indicator function $c: X \to \{0, 1\}$.
* **Training Examples ($D$):** A set of instances from $X$, each paired with its correct classification given by the target concept, i.e., $D = \{(x_1, c(x_1)), (x_2, c(x_2)), ...\}$.
* **Hypothesis Space ($H$):** The set of all possible concepts that the learning algorithm is allowed to consider. The output of the learner is a hypothesis $h \in H$, where $h: X \to \{0, 1\}$, which is intended to be the best approximation of the target concept $c$.

## Example 
| Month  | Temp | Humidity | Wind   | Go Surfing? (c(x)) |
| :----- | :--- | :------- | :----- | :----------------- |
| July   | Cold | Low      | Strong | **Yes**            |
| August | Hot  | Low      | Strong | **Yes**            |
| July   | Hot  | Low      | Weak   | **No**             |
| Sept.  | Cold | High     | Weak   | **No**             |
**Target Concept $(c)$**: A true rule that defines a good day for surfing. 
Assume that the unknown rule is simple "**any day with strong wind**"
