---
title: Maximum Likelihood vs Maximum A Posteriori in action
draft: false
tags: []
---

![[Pasted image 20240815154703.png|center|400]]
**Specify for the following figure, how the *Maximum likelihood* decision rule applied to to the red class and to the blue class, respectively, will decide**

- [[240402 Maximum Likelihood Decision Rule|ML Classifier]] chooses the class with the the highest Likelihood $p(x|s)$ 
- From Graph it is visible that
	- $0<X<11$, $p(x|s=2)$ has the highest value. => Classification is RED
	- $11<X<17$, $p(x|s=2)$ has the highest value. => Classification is BLUE

---

**Now let the red class be only $1 / 3$ as frequent as the blue class**

$$
\mathrm{P}(s=2)=\frac{1}{3} \cdot \mathrm{P}(s=1)
$$

**Specify depending on the feature $x$, to which class the *[[240402 Maximum Likelihood Decision Rule|ML]]* classifier, and to which class the *[[240815 Bayes Decision Rule or Maximum A Posteriori|MAP]]* classifier decides.**

[[240815 Bayes Decision Rule or Maximum A Posteriori|MAP]] uses the Prior which can be calculated as follows

Given: $P(s=2) = \dfrac 1 3 \cdot P(s=1)$

![[../Files/Pasted image 20240818161746.png|center|800]]
From the Prior the decision boundary can be expected to shift with the new decision boundary $x*$
The Decision Boundary in [[240815 Bayes Decision Rule or Maximum A Posteriori|MAP]] is where the [[240410 Bayes Classifier|Posterior]] Probabilities are equal.

![[../Files/Pasted image 20240818163835.png]]
- $x < x*$ i.e. $3\cdot p(x|s=1) < p(x|s=2)$, [[240815 Bayes Decision Rule or Maximum A Posteriori|MAP]] chooses red class
- $x > x*$ i.e. $3\cdot p(x|s=1) > p(x|s=2)$, [[240815 Bayes Decision Rule or Maximum A Posteriori|MAP]] chooses blue class 

The exact value of $x*$ is where $3p(x|s=1) = p(x|s=2)$, which appears to be around $x= 11.9$ in the graph. 




