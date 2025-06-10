---
title: Pooling Functions
draft: false
tags: 
date: 2025-04-22
---

## Definition

Pooling functions reduces the spatial dimensions (width and height) of the input volume while preserving the most important features. 

### Max Pooling

Selects the maximum value from the region covered by the filter. Good for detecting sharp features like edges.
**Example:** From values [1, 3, 2, 4], max pooling returns 4. 

### Average Pooling

Calculates the average of all values in the region covered by the filter. Better for preserving background features.

**Example:** From values [1, 3, 2, 4], average pooling returns 2.5

## Use case

- Reduce computation by decreasing dimensions
- Extract dominant features
- Provide some translation invariance
- Reduce overfitting