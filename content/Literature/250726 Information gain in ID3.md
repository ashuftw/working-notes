---
title: Information Gain in ID3
draft: false
tags: 
date: 2025-07-26
---
**Information gain** is the criterion used by the ID3 decision tree algorithm to choose which attribute to select at each step of building the tree. It measures the reduction in entropy (or uncertainty) about the classification of training examples after the set has been partitioned on a specific attribute. The attribute with the highest information gain is chosen. 

The computation is based on **Shannon Entropy**:

1. First, the **entropy** of a set of instances $S$, with respect to a binary classification, is calculated as:

$$
S = -p_{\oplus} \log_2 p_{\oplus} - p_{\ominus} \log_2 p_{\ominus}
$$

where,
	- $p_{\oplus}$-> is the proportion of positive examples.
	- $p_{\ominus}$ -> is the proportion of negative examples in $S$. 
2. Next, for a given attribute $A$, the set $S$ is partitioned into subsets $S_v$ for each possible value $v$ of $A$. The remaining entropy after the split is the weighted average of the entropies of these subsets:

		$$
		S_A = \sum_{v \in \text{Values}(A)} \frac{|S_v|}{|S|} S_v
		$$

		where,
	- $|S_v|$ -> number of instances in the subset with value $v$.
	- $|S|$ -> is the total number of instances. 
3. Finally, the **information gain** for attribute $A$ is the entropy of the original set minus the remaining entropy after splitting on $A$:

		$$
		Gain(S, A) = S - S_A
		$$
