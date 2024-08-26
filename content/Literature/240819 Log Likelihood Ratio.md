---
title: Log Likelihood Ratio
draft: true
tags:
---
 
$$
\text{LLR}(\mathbf x)=\log \frac{P(\mathbf{x} \mid s=1)}{P(\mathbf{x} \mid s=2)}
$$


## Example
A 2-class Bayes classifier is realized by comparing the log-likelihood ratio (LLR) to a fixed threshold value $\theta$ :

$$
\text{LLR}(x) \lessgtr \theta
$$

Interpret the choice of the threshold value for the cases $\theta = 0$ and $\theta = 1$  

Hint:

$$
g(x) = \log \frac{P(x|s=1)}{P(x|s=2)} + \log \frac{P(s=1)}{P(s=2)}
$$


---

![[../Files/Pasted image 20240819122252.png]]

![[../Files/Pasted image 20240819124002.png|center]]


---
# References
[[Private/Excalidraw/Drawing 2024-08-19 12.05.49.excalidraw.md#^JEVRL-PwRECHjrQpPAmtn|Source]]