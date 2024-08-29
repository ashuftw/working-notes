---
title: Computation of Variables in a Bayesian Belief Network
draft: false
tags:
---
## Example 1 

![[../Files/Pasted image 20240820112047.png|center|425]]


$$
\mathrm{P}(e)=\sum_{d \in \mathcal{D}} \mathrm{P}(e \mid d) \cdot \underbrace{\sum_{c \in \mathcal{C}} \sum_{a \in \mathcal{A}} \mathrm{P}(d \mid c, a) \cdot \mathrm{P}(a) \cdot \overbrace{\sum_{b \in \mathcal{B}} \mathrm{P}(c \mid b) \cdot \mathrm{P}(b)}^{\mathrm{P}(c)}}_{\mathrm{P}(d)}
$$

-  **Node A:** $P(a)$
-  **Node B:** $P(b)$
-  **Node C:** $P(c) = \sum_{b \in B} P(c|b) \cdot P(b)$
-  **Node D:** $P(d) = \sum_{a \in A} \sum_{c \in C} P(d|a,c) \cdot P(a) \cdot P(c)$
-  **Node E:** $P(e) = \sum_{d \in D} P(e|d) \cdot P(d)$
## Example 2 
![[../Files/Pasted image 20240820131142.png|center|450]]

- **Specify the probability $\mathrm{P}(A, B, C, D, E)$ by using the single terms of the Bayesian belief network (hint: First reorder the terms!)**
	![[../Files/Pasted image 20240820132045.png|center]]
- **Now let $C$ be an unknown and the probability for $D$ be inquired.Write down the probability $\mathrm{P}(D \mid A, B, E)$ by using the single terms of the Bayesian belief network.**

## Example 3 
![[../Files/Pasted image 20240820122828.png|center|450]]

**Given:** $P(C)$ is unknown 
WRONG
![[../Files/Pasted image 20240821110233.png|center]]


[[Private/Excalidraw/Drawing 2024-08-20 12.30.43.excalidraw.md#^group=_RcEI7sUYhhXIDVItK--f|source]]

