---
title: Activation Function for a Bayesian Classifier
draft: false
date: 2024-05-10
---

## Assignment of Nodes 
![[Pasted image 20240610165943.png|center|400]]

The Output nodes are assigned such that each node represents one particular class in the classification problem.  
## Softmax (Normalized Exponential)

$$
y_i=\frac{e^{v_i}}{\sum_{j=1}^N e^{v_j}} \in[0,1]
$$

Where, 
- $v_i\rightarrow$ It is the output from the Hidden Layer before applying the activation function. 


