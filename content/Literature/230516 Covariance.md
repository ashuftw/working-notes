---
title: Covariance
draft: false
date: 2023-05-16
---

## **Definition**
- It is the mean value of the product of the deviations of two random variables from their respective means. 
- It is a statistical measure that quantifies how changes in one variable are associated with changes in another variable. 

**Mathematically**


$$
\begin{align*} \operatorname{cov}[X, Y] & = \mathbb{E}[(X - \mathbb{E}[X])(Y - \mathbb{E}[Y])] \\ & = \mathbb{E}[XY - X\mathbb{E}[Y] - \mathbb{E}[X]Y + \mathbb{E}[X]\mathbb{E}[Y]] \\ & = \mathbb{E}[XY] - \mathbb{E}[X\mathbb{E}[Y]] - \mathbb{E}[\mathbb{E}[X]Y] + \mathbb{E}[\mathbb{E}[X]\mathbb{E}[Y]]. \end{align*}
$$

Now, using the linearity of expectations:

$$
\operatorname{cov}[X, Y]  = \mathbb{E}[XY] - \mathbb{E}[X]\mathbb{E}[Y] - \mathbb{E}[X]\mathbb{E}[Y] + \mathbb{E}[X]\mathbb{E}[Y]
$$


$$
\boxed{\operatorname{cov}[X, Y]= \mathbb{E}[XY] - \mathbb{E}[X]\mathbb{E}[Y]}
$$


where $\mathbb{E}[X Y]=\int_{\mathbb{R}} \int_{\mathbb{R}} x y \, f_{X, Y}(x, y) \, d x d y$. 
### Conditions
- $\operatorname{cov}[X, Y] > 0:$ As $X$ increases, $Y$ tends to increase, and as $X$ decreases, $Y$ tends to decrease. The variables have a positive linear relationship.
- $\operatorname{cov}[X, Y] < 0:$ Indicates that as $X$ increases, $Y$ tends to decrease, and as $X$ decreases, $Y$ tends to increase. The variables have a negative linear relationship.
- $\operatorname{cov}[X, Y] = 0:$ No linear relationship between $X$ and $Y$ (Uncorrelated). However, it does not necessarily imply independence between the variables.
	![[Pasted image 20231122114202.png|center]]

### Note
- $\text{cov}[X,X]=\text{var}[X]$
	The covariance of a Random variable with itself gives the dispersion of $X$ around it's mean value. 

