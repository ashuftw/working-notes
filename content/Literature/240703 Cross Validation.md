---
title: Cross Validation
draft: false
date: 2024-07-03
---
## Use case 
Cross validation is a technique used to estimate the true generalization error. 
## Types 

1. **Leave One Out Cross Validation** 
	- A datum is removed from the the data and the model is trained on it. 
	- Repeat this for each datum and average the errors. 
	- Thus a truly unbiased error of the model is obtained. 
	- However, not feasible. 
2. **K-fold Cross Validation**
	 ![[../Files/Pasted image 20240703131751.png|center|550]]
	- It is an alternative to **Leave One Out** method and provides a good approximation. 
	- Here instead of individually removing a datum and training the remaining the data, the data set is split into $(k-1)$ Training set with one Test set. 
	- The error is computed for each set and averaged. 
	- The whole process is the repeated with a different Test Set. 

