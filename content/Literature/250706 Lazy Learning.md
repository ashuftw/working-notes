---
title: Lazy Learning
draft: true
tags: 
date: 2025-07-26
---
**Lazy learning** is a machine learning approach where the system stores the training samples and postpones computation until it receives a new query.


In lazy learning, instead of building a general model during a training phase, it performs the generalization work at runtime by recombining the saved training samples to determine the output for the new example.

## Approaches to Lazy Learning
Simple approaches to lazy learning are typically variations of the **Nearest Neighbor** algorithm. The main variations are:

* **Nearest Neighbor:** This is a basic method where a new input is assigned the output of its single closest training sample.
* **K-Nearest Neighbors (k-NN):** A more robust approach that averages over the *k* nearest neighbors to produce an output. For regression, this is often the mean of the neighbors' values.
* **Weighted K-Nearest Neighbors:** This method enhances k-NN by weighting the contribution of each of the k neighbors according to its distance from the query point, giving closer neighbors more influence.

## Induction Bias
The **inductive bias** of lazy learning algorithms like **k-NN** is the assumption that "close" inputs should lead to "similar" outputs. The definition of "close" is determined by the choice of the distance measure (metric), which is therefore a crucial part of this bias.