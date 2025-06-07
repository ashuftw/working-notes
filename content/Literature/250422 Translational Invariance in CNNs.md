---
title: Translational Invariance in CNNs
draft: false
tags: 
date: 2025-04-22
---
CNNs have **translation invariance/equivariance**, which allows them to recognize objects regardless of their precise location in the image.

This two architectural elements that create this property are:

1. **Shared filter weights / Kernels:** The same convolutional filters are applied across the entire image, meaning a feature detector that works in one position will work in all positions.
2. **Pooling operations:** These reduce the spatial dimensions of the input volume/ feature map and provide some invariance to small translations by summarizing features in local regions.