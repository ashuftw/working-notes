---
title: Intersection over Union (IoU)
draft: false
tags:
---
It is a Quality Measure used in [[240821 Semantic or Image Segmentation|Image Segmentation]]. 

Visually, it can be represented as follows. 

![[../Files/Pasted image 20240821112634.png|center|650]]

Using the Pixels that fall in the intersection between [[240429 Binary Classifications|FP, TP and FN]] pixel classifications, an accurate Image Segmentation can be obtained. 

## Mathematically
- **Intersection over union ($\text{IoU}$):** 
$$
\boxed{ \mathrm{IoU}=\frac{\mathrm{TP}}{\mathrm{TP}+\mathrm{FN}+\mathrm{FP}}}
$$

Here the Binary classification is directly used for calculation of IoU. Hence it is biased towards classifications of with large $\text{TP}$ and $\text{FN}$ counts. 
- **Instance-level intersection over union ($\text{iIoU}$):**
	
$$
\boxed{\mathrm{iIoU}=\frac{\mathrm{iTP}}{\mathrm{iTP}+\mathrm{iFN}+\mathrm{FP}}}
$$

	Here the $\text{TP}$ and $\text{FN}$ are weighted by the ratio of the average class instance size by the current ground truth size instance. 





