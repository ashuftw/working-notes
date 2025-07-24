---
title: Bayesian Approach for Two Classes
draft: false
tags: 
date: 2025-07-19
---
The [[250711 Bayesian Approach  to Classification|Bayesian Approach Classification]] is an indirect probabilistic method for classifying a data point $x$ into one of two classes, $C_1$ or $C_2$.
### Steps:

1.  **Model Class-Conditional Likelihoods:**
    * $p(x \mid C_1)$
    * $p(x \mid C_2)$

2.  **Model Prior Probabilities:**
    * $p(C_1)$
    * $p(C_2)$ (Note: $p(C_1) + p(C_2) = 1$)

3.  **Calculate Posterior Probabilities (using Bayes' Formula):**
    * For Class 1:
        

    	$$
    	p(C_1 \mid x) = \frac{p(x \mid C_1) p(C_1)}{p(x)}
    	$$


    * For Class 2:
        

    	$$
    	p(C_2 \mid x) = \frac{p(x \mid C_2) p(C_2)}{p(x)}
    	$$


    * Where $p(x)$ (the evidence) is the normalization constant:
        

    	$$
    	p(x) = p(x \mid C_1) p(C_1) + p(x \mid C_2) p(C_2)
    	$$



### Classification Decision:

Classify $x$ into the class with the highest posterior probability:

* If $p(C_1 \mid x) > p(C_2 \mid x)$, then $x \in C_1$.
* If $p(C_2 \mid x) > p(C_1 \mid x)$, then $x \in C_2$.