---
title: Linear Discriminant Function
draft: false
tags: 
date: 2025-08-15
---
### Definition
A **linear discriminant function** is a function used in pattern classification to separate data into two or more classes. Its output is a linear combination of the input features. Geometrically, it defines a [[250711 Hyper planes|hyperplane]] that acts as a decision boundary between classes.

### Mathematical Expression
For a $d-$dimensional input feature vector $\mathbf x$, a linear discriminant function $g(x)$ is defined as:

$$ g(\mathbf{x}) = \mathbf{w}^T\mathbf{x} + w_0 $$

Where:
- $\mathbf x$: The input feature vector, $\mathbf{x} = [x_1, x_2, ..., x_d]^T$.
- $\mathbf w$: The weight vector, $\mathbf{w} = [w_1, w_2, ..., w_d]^T$.
- $w_0$: The bias or threshold.
- $\mathbf{w}^T\mathbf{x}$: The dot product of the weight and feature vectors, which is $\sum_{i=1}^{d} w_i x_i$.

---
## Application in Classification

### Two-Class Case
For a problem with two classes, a single linear discriminant function is used to make a decision:
- Assign **x** to **Class 1** if $g(\mathbf{x}) > 0$.
- Assign **x** to **Class 2** if $g(\mathbf{x}) < 0$.
- If $g(\mathbf{x}) = 0$, the vector **x** lies directly on the decision boundary.

### Multi-Class Case
For a problem with `N` classes, `N` linear discriminant functions are used, one for each class: $g_1(\mathbf{x}), g_2(\mathbf{x}), ..., g_N(\mathbf{x})$.

The decision rule is to assign the input vector **x** to the class `i` for which the corresponding discriminant function $g_i(\mathbf{x})$ has the highest value:

**Assign x to class `i` if $g_i(\mathbf{x}) > g_j(\mathbf{x})$ for all $j \neq i$.**