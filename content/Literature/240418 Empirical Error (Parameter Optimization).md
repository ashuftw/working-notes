---
title: Empirical Error (Parameter Optimization)
draft: false
tags:
---
  
## Definition 
It is the error or leeway that is taken while training a model (Parameter Optimization in the model). The purpose of the Empirical error is to prevent overfitting (where the model even predicts the noise in the data) and make it more generalisable. 
**Quadratic error function or Empirical Quadratic loss**

$$
\boxed{
E(\mathbf{w})=\frac{1}{2N} \sum_{n=1}^N\left(y\left(x_n, \mathbf{w}\right)-t_n\right)^2
}
$$


![[Pasted image 20240418160819.png]]