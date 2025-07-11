---
title: 1 of K Encoding Scheme
draft: false
tags: 
date: 2025-07-10
---

## Definition

It is a technique use to model labels for **multi-class** problems. 
Here, each label $t_i$, is represented as a vector with $K$ dimensions, corresponding to the $K$ available classes.

The vector consists of all zeros except for a single $1$ at the position indicating the correct class.

For an input $x_i$ belonging to class $C_k$, the label vector $t_i$ is defined as:

$$t_i=\left(t_1, \ldots, t_k, \ldots, t_K\right)=(0, \ldots, 1, \ldots, 0)$$

where the $k-$th element is $1$.

This $1-$of$-K$ label vector can also be interpreted as a probability vector. An example of this is the DeepFace system, which uses a "one-of-4030" encoding for its 4,030 face classes.

### Example 
Classification of images into one of three categories: **Cat**, **Dog**, or **Bird ** i.e **(K=3)** classes. According to the 1-of-K encoding scheme, the label for each image will be a 3-dimensional vector.

**Label Modeled for an image from each class:**
- If an input image $x$ is a Cat (Class 1), its label vector $t$ would be:
    $t =(1, 0, 0)$
- If an input image $x$ is a Dog (Class 2), its label vector $t$ would be:
    $t=(0, 1, 0)$ 
- If an input image $x$ is a Bird (Class 3), its label vector $t$ would be:
    $t = (0, 0, 1)$

Each vector has a '$1$' in the position corresponding to its class and '$0$'s in all other positions.