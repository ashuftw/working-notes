---
title: Intersection over Union (IoU)
draft: false
date: 2024-08-21
---

It is a Quality Measure used in [[240821 Semantic or Image Segmentation|Image Segmentation]]. 

Visually, it can be represented as follows. 

![[../Files/Pasted image 20240821112634.png|center|650]]

Using the Pixels that fall in the intersection between [[240429 Binary Classifications|FP, TP and FN]] pixel classifications, an accurate Image Segmentation can be obtained. 

### Intersection over union ($\text{IoU}$)



$$
\boxed{ \mathrm{IoU}=\frac{\mathrm{TP}}{\mathrm{TP}+\mathrm{FN}+\mathrm{FP}}}
$$



- Simply measures overlap between predicted segmentation and ground truth
- Problem: Large objects have more pixels, so they dominate the score

### Instance-level intersection over union ($\text{iIoU}$)



$$
\boxed{\mathrm{iIoU}=\frac{\mathrm{iTP}}{\mathrm{iTP}+\mathrm{iFN}+\mathrm{FP}}}
$$



- Modifies IoU to treat objects more fairly regardless of their size
- Weights each object by: (average object size) / (this object's size)
- Makes segmenting small objects just as important as large ones

