---
title: Binary Classifications
draft: false
date: 2024-04-29
---

#### True Positive 
It is an instance where the model correctly predicts the positive class i.e, the Model predicts a true value given that the answer is actually true. 
- **True Positive Rate**
	It is the ratio of the number of True Positive classifications to the actual number of positives.  
	
$$
TPR=\dfrac{TP}{TP+FN}
$$

	> Note: Also called *Hit Rate* or *Recall*
#### False Positive
It is an instance where the classifier incorrectly predicts a positive class.  i.e, the Model predicts a true value given that the actual answer is false. 
- **False Positive Rate**
	It is the ratio of the number of False Positive classifications to actual number of negatives. 
	
$$
FPR=\dfrac{FP}{FP+TN}
$$

	> Note: Also called *False Acceptance Rate (FAR)*
#### True Negative 
It is an instance where the model correctly predicts a negative class. 
- **True Negative Rate**
	It is the ratio of the number of Negative classifications to the actual number of negatives. 
	
$$
TNR=\dfrac{TN}{TN+FP}=1-FPR
$$

	> Note: Also called *Specificity*
#### False Negative 
It is an instance where the Model incorrectly predicts a Negative class. 
- **False Negative Rate**
	It is the ratio of the number of False Negative classifications to actual number of false negatives. 
	
$$
FNR=\dfrac{FN}{FN+TP}
$$

	> Note: Also called *False Rejection Rate* or *Miss Rate*
 


| Object         | ML Term                          |
| -------------- | -------------------------------- |
| True Positive  | Hit rate / Recall                |
| False Positive | False Acceptance Rate            |
| True Negative  | Specificity                      |
| False Negative | False Rejection Rate / Miss Rate |


