---
title: Receiving Operator Characteristics
draft: false
date: 2024-08-21
---

## $\text{TPR = f(FPR)}$
![[../Files/Pasted image 20250423174738.png|center|700]]
Here $\theta$ represents the classification threshold of your binary classifier, e.g. [[240423 Likelihood Ratio|Likelihood Ratio]]. 

**Note**
When theta is high (at the bottom-left of the curve):
- The classifier requires stronger evidence to predict the positive class
- You get fewer false positives but also fewer true positives

As theta decreases (moving toward the top-right of the curve):
- The classifier becomes more lenient in predicting the positive class
- You get more true positives but also more false positives
- This results in higher recall but lower precision

[[Private/Excalidraw/Drawing 2024-08-21 12.09.32.excalidraw.md#^group=xaJKKCGmZJTEpHxRtQBc-|source]]

