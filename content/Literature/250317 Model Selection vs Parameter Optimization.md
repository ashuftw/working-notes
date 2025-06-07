---
title: Model Selection vs Parameter Optimization
draft: true
tags: 
date: 2025-03-17
---
- **Model selection**: Choosing **which model** to use (e.g., Linear Regression vs. Decision Tree).
- **Parameter optimization**: Finding the **best settings** for the chosen model (e.g., adjusting max depth in Decision Tree).

### Example: Predicting House Prices
We predict house prices based on features like area, number of bedrooms, and location.
**Model Selection**

We need to choose the best model:
- **Linear Regression** (if the relationship is simple and linear)
- **Decision Tree** (if the data has complex patterns)
- **Neural Network** (if we have a lot of data and non-linear relationships)

We compare these models and select the one with the best performance.

**Parameter Optimization**
After selecting **Decision Tree**, we fine-tune its **hyperparameters**, such as:
- **Max Depth** (how deep the tree should be)
- **Min Samples Split** (minimum data points needed to split a node)

This step improves the model’s accuracy and prevents overfitting.