---
title: Relationship between K-means and Expectation Maximization Algorithms
draft: false
tags: 
date: 2025-07-27
---
[[250727 K-means Algorithm|K-means]] is a simplified version of the Expectation-Maximization (EM) algorithm.

* **E-step (Expectation)**: This is the assignment step. For fixed prototypes, each data point is assigned to the nearest cluster. This is equivalent to calculating which cluster is "expected" for each point.

	$$
	r_{nk} = \begin{cases} 1 & \text{if } k = \text{argmin}_j ||x_n - w_j||^2 \\ 0 & \text{otherwise} \end{cases}
	$$

* **M-step (Maximization)**: This is the update step. With the cluster assignments fixed, the prototypes are moved to the mean of their assigned data points. This new position maximizes the similarity to the assigned points (i.e., minimizes the error J for the given assignments).

	$$
	w_k = \frac{\sum_{n=1}^{N} r_{nk} x_n}{\sum_{n=1}^{N} r_{nk}}
	$$
