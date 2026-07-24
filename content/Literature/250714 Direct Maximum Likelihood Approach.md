---
title: Direct Maximum Likelihood Approach
draft: false
tags: 
date: 2025-07-14
---
The [[250714 Direct Maximum Likelihood Approach|Direct Maximum Likelihood Approach]] for Labels is a method to directly map data to class labels. This approach requires labeled data, denoted as $\left(x_n, t_n\right)$ where $t_n$ is the class label. It operates under the assumption that the class-conditional probability $p\left(x \mid C_k\right)$, is normally distributed, and for a two-class problem, the labels are:

$$
t_n \in\{0,1\} .
$$


## Maximizing Likelihood
The objective is to find the model parameters ($\left.\pi, \mu_1, \mu_2, \Sigma\right)$ that maximize the label-data-likelihood function, which is given as:

$$
L\left(\pi, \mu_1, \mu_2, \Sigma\right)=\prod_n\left[\pi \mathcal N\left(x \mid \mu_1, \Sigma\right)\right]^{t_n}\left[(1-\pi) \mathcal N\left(x \mid \mu_2, \Sigma\right)\right]^{1-t_n}
$$

## Computational Tricks
Instead of maximizing the likelihood function directly, we maximize the logarithm. We also remove all parameters that don't depend on the specific parameter that's being optimized. (Valid because these terms will become zero during differentiation). 

For instance, to find the optimal parameter $\pi$, 

$$
\arg \max _{\pi}   \sum_n\left(t_n \ln (\pi)+\left(1-t_n\right) \ln (1-\pi)\right)
$$

Where,
- $\pi$ is the proportion of data belonging to the first class (**prior probability** for class $C_1$ or $P(C_1)$) 



	$$
	\pi = \frac{1}{N} \sum_n t_n = \frac{N_1}{N}
	$$




- $N$ is the total number of data points
- $N_1$ is the total count of data points in class $C_1$
- $t_n$ is the label for the $n-$th data point, $x_n$. ([[250710 One of K Encoding Scheme|One of K Encoding Scheme]])

**Example**:
if $40$ out of $100$ data points in your training set belong to class $C_1$​, the formula gives you: $\pi=\frac{100}{40}​=0.4$

