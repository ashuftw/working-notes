---
title: Linear Learning Models
draft: true
tags: 
date: 2025-03-17
---

### Definition

A model is considered linear when it is linear in its parameters, *regardless* of whether it's linear in the inputs.
Specifically, a model is linear if:
- It can be expressed as a linear combination of the parameters
- The output is a weighted sum of basis functions y(x) = Σ wⱼφⱼ(x)

**Examples**
1. Simple linear regression: y(x) = w₀ + w₁x
    - Linear in both parameters and input
2. Polynomial regression: y(x) = w₀ + w₁x + w₂x² + ... + wₙxⁿ
    - Linear in parameters (w₀, w₁, w₂, ...) but non-linear in input x

