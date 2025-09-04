---
title: Nadaraya Watson Regressor
draft: false
tags: 
date: 2025-07-26
---
The Nadaraya-Watson kernel regression estimator uses kernel functions for weighting and is defined by the following formula


$$
f(x_{q})=\sum_{i}y_{i}\frac{K_{\sigma}(x_{i}-x_{q})}{\sum_{j}K_{\sigma}(x_{j}-x_{q})}
$$


The key parameter that has to be chosen is the **bandwidth $\sigma$** of the kernel function, $K_{\sigma}$ (often a Gaussian kernel). This parameter controls the width of the kernel and thus the smoothness of the resulting function.
- $f(x_q)$ -> Final **predicted output value** for the new, unseen input point $x_q$.
- **$x_q$** -> **query point**, which is the new input for which you want to make a prediction.
- **$K_{\sigma}(x_i - x_q)$**: This is the **kernel function**. It measures the similarity or "closeness" between a training point $x_i$ and the new query point $x_q$. The result is a scalar value that is typically large when the points are close and small when they are far apart. A common choice is the Gaussian kernel.
- **$\frac{K_{\sigma}(x_{i}-x_{q})}{\sum_{j}K_{\sigma}(x_{j}-x_{q})}$**: This entire fraction acts as a **normalized weight**. The numerator is the similarity of a single training point, and the denominator is the sum of similarities over all training points. This ensures all the weights sum to 1. The weight assigned to a training output $y_i$ is directly proportional to the similarity between its corresponding input $x_i$ and the query point $x_q$.

