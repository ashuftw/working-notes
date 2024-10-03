---
title: Equal Error Rate
draft: false
date: 2024-08-21
---

## $\text{FNR = f(FPR)}$
### Equal Error Rate
It is the point on the [[240821 Receiving Operator Characteristics|ROC]] curve where the False Positive Rate equals the False Negative Rate.
The Bayes classifier will operate at the EER point when:
- **Equal Priors**
	When the prior probabilities are equal, the Bayes decision rule simplifies to comparing only the likelihoods. This creates a balanced starting point for classification.
- **Cost of mis-classification is equal**
	 If the cost of a false positive equals the cost of a false negative, the Bayes classifier won't be biased towards minimizing one type of error over the other.

![[../Files/Pasted image 20240821132543.png|center|600]]


### Applications of the having the Operating Condition on the Right side of the EER Curve
- Medical screening tests for serious diseases: It's often preferable to have more false positives (which can be ruled out with further testing) than to miss actual cases of a dangerous disease.
- Fraud detection in financial transactions: Banks may prefer to flag more transactions as potentially fraudulent for review, even if some are legitimate, rather than miss actual fraud attempts.

[[Private/Excalidraw/Drawing 2024-08-21 12.09.32.excalidraw.md#^group=xaJKKCGmZJTEpHxRtQBc-|source]]





