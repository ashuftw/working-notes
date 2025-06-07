---
title: MAP with Gaussian Prior
draft: false
tags: 
date: 2025-03-17
---
### To get the MAP parameters

1. **MAP definition:**
$$ 
w_{MAP} = \arg\max_w P(w|D) = \arg\max_w P(D|w)P(w)
$$ 
2. **For Gaussian case, this becomes:**
$$
w_{MAP} = \arg\min_w \left[\frac{1}{2}\sum_n (t_n - w^T\phi(x_n))^2 + \frac{\lambda}{2}||w||^2\right]
$$    
3. **Remember:** This is just **squared error + L2 regularization**!
4. **Linear model solution:**  
$$
w_{MAP} = (\lambda I + \Phi^T\Phi)^{-1}\Phi^T t
$$

> **Key to remember:** MAP = ML + regularization (prior acts as regularizer)

**Note:**
- **Simple linear**: $y(x, w)=w^T x=w_0+w_1 x_1+\ldots$
- **Polynomial:** $y(x, w)=w^T \phi(x)$ where $\phi(x)=\left[1, x, x^2, \ldots\right]$
- **RBF:** $y(x, w)=w^T \phi(x)$ where $\phi(x)=\left[\exp \left(-\left\|x-\mu_1\right\|^2\right), \ldots\right]$
