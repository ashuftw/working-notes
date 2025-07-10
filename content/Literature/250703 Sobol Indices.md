---
title: Sobol Indices
draft: false
tags: 
date: 2025-07-03
---
[[250703 Sobol Indices|Sobol indices]] are a way to measure how much sensitive the output of a model is for different inputs. In other words, it quantifies how much each uncertain input parameter contributes to the output variance. They are the main tool for **global sensitivity analysis** and come in two types:
### First-Order Sobol Index ($\text{Si}$)
It measures the direct effect of a single input variable $X_i$ to the output variance. It tells you how much the output would change, on average, if you only varied that one input and kept the others at their average values. 
$$
S_i=\frac{D_i}{V[M(X)]}
$$
Where:
- $D_i$ is the partial variance caused by the input factor $X_i$ alone. These terms are derived from an ANOVA-like decomposition of the model function.
- $V[M(X)]$ is the total variance of the model output.

### Total Effect Index ($\text{S}_{Ti}$)
It measures the total impact of an input variable $X_i$, both its direct effect and all its interaction with other inputs. A high total effect index indicates that a variable is influential, either by itself or through its combined effects with other variables. 

$$
\text{Total Impact of Input Variable}=\frac{\text{sum of all variance components}}{\text{total variance}}
$$
Mathematically, 
$$
S_{T i}=\frac{D_i+\sum_{j \neq i} D_{i j}+\sum_{j \neq i, k \neq i, j<k} D_{i j k}+\ldots}{V[M(X)]}
$$


### Intuition
![[../Files/IMG_20250704_150030060.jpg|center|600]]
**Solo Effect**
How will changing the quantity of the Sugar affect how sweet the cake is if we keep the rest of the ingredients more or less the same portions each time. 
**Interaction effect**
How will changing the Sugar quantity affect how sweet the cake is give that we have different quantities of cocoa. Example: Maybe with a lot of cocoa, we need to use lots of sugar! 

1. **First Order Sobol**->Tracks the solo effect. 
2. **Total Effect**-> Tracks both Solo and Interaction Effect. 