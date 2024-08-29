---
title: Bayes Theorem
draft: false
tags:
---
  
## Use-case
The Base theorem gives an interface to revise pr-existing theories or hypothesis (Prior) with given new evidence. 

$$
\text { posterior }=\frac{\text { likelihood } \times \text { prior }}{\text { evidence }} \text {. }
$$


$$
\boxed{P(H \mid E)=\frac{P(E \mid H) P(H)}{P(E)}}
$$

Where, 
- $P(H|E)$, **Posterior Probability** is the probability of Hypothesis $H$ given that the evidence $E$ has occurred. (Note: $H$ is one event in the sample space.)
- $P(E|H)$, **Likelihood** is the Probability of the evidence occurring give that the Hypothesis $H$ is true. 
- $P(E|H),$ **Prior** is the Probability of a Hypothesis that we assume or know before any data is taken into consideration. 
- $P(E)$, **Evidence** is the Probability of the evidence regardless of the Hypothesis. 
> **Note:** The Posterior Probability is a calculated value based on new evidence. 

In Pattern recognition, the Hypothesis would be the Class and the Evidence would be the features used to make the classification. 



