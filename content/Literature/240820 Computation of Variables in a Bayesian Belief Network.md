---
title: Computation of Variables in a Bayesian Belief Network
draft: false
date: 2024-08-20
---

## Example 1 

**Decompose $\text P(A, B, C, D)$ step by step according to the chain rule into as many terms as possible and simplify, if $A$ and $B$ are independent of $C$ and $D$.**

![[../Files/Pasted image 20240820112047.png|center|425]]

Given that $A$ and $B$ are independent of $C$ and $D$, we can decompose $P(A,B,C,D)$ using the chain rule and then simplify using this independence property.

Chain rule decomposition



$$
P(A,B,C,D) = P(A|B,C,D) \times P(B|C,D) \times P(C|D) \times P(D)
$$



Since $A$ and $B$ are independent of $C$ and $D$:
- $P(A|B,C,D) = P(A|B)$
- $P(B|C,D) = P(B)$

Substitute:



$$
P(A,B,C,D) = P(A|B) \times P(B) \times P(C|D) \times P(D)
$$



Since $A$ and $B$ are independent:
- $P(A|B) = P(A)$

Finally



$$
P(A,B,C,D) = P(A) \times P(B) \times P(C|D) \times P(D)
$$



## Example 2 

![[../Files/Pasted image 20240820131142.png|center|450]]

- **Specify the probability $\mathrm{P}(A, B, C, D, E)$ by using the single terms of the Bayesian belief network (hint: First reorder the terms!)**




	$$
	P(E,D,A,C,B) = P(E|D) \cdot  P(D|A,C) \cdot  P(C|B) \cdot  P(A) \cdot  P(B)
	$$




- **Now let $C$ be an unknown and the probability for $D$ be inquired.Write down the probability $\mathrm{P}(D \mid A, B, E)$ by using the single terms of the Bayesian belief network.**




	$$
	P(D|A,B,E) = P(E|D) \quad \sum_C \left[P(D|A,C) \cdot P(C|B)\right ]\quad  \left(  P(A) \cdot P(B)\right)
	$$




## Example 3 

![[../Files/Pasted image 20240820122828.png|center|450]]

**Given:** Calculate $C$ using the entire network 

Joint probability using chain rule:



$$
P(A,B,C,D) = P(D|C,B) \cdot P(C|A) \cdot P(B|A) \cdot P(A)
$$



Marginalize over A, B, and D to get P(C):



$$
P(C) = \sum_{d\in D}\sum_{b\in B}\sum_{a\in A} P(D|C,B) \cdot P(C|A) \cdot P(B|A) \cdot P(A)
$$



1. Since $\sum_{d}P(D|C,B)  = 1$ (sum of probabilities over all possible values of D):




	$$
	P(C) = \sum_{b\in B}\sum_{a\in A} P(C|A) \cdot P(B|A) \cdot P(A)
	$$




2. Since $\sum_b P(B|A) = 1$ (sum of probabilities over all possible values of B):




	$$
	P(C) = \sum_{a\in A} P(C|A) \cdot P(A)
	$$




---
Slightly wrong Solution: 
[[Private/Excalidraw/Drawing 2024-08-20 12.30.43.excalidraw.md#^group=_RcEI7sUYhhXIDVItK--f|source]]

