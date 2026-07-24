---
title: Bayesian Approach to Classification
draft: false
tags: 
date: 2025-07-11
---
The Bayesian approach is an indirect method for classification that models probabilities to determine class membership. It involves three main steps:
1. Model the class-conditional likelihood for each class,




	$$
	p\left(x \mid C_k\right) .
	$$




2. Model the prior probability for each class,




	$$
	p\left(C_k\right) .
	$$




3. Use Bayes' formula to calculate the posterior probability, $p\left(C_k \mid x\right)$, which is the probability of a class given the input data.

The [[240410 Bayesian Classifier|Bayesian Formula]] is:

$$
p\left(C_k \mid x\right)=\frac{p\left(x \mid C_k\right) p\left(C_k\right)}{p(x)}
$$


Here, $p(x)$ is the "evidence" and acts as a scaling factor that does not influence the classification decision.