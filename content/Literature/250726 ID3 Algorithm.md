---
title: ID3 Algorithm
draft: false
tags: 
date: 2025-07-26
---
It is a method of constructing [[250726 Decision Tree|Decision Tree]] from a set of data. 

## Organisation of Search 
- The ID3 algorithm employs a **"greedy,"** simple hill-climbing search.
- This search method **doesn't look ahead or backtrack**.
- At each node, the algorithm assesses all unused attributes to find the one with the **highest [[250726 Information gain in ID3|information gain]]**.
- It "greedily" selects the best attribute to create the decision rule for that specific node.
- This is an **incomplete search** because it commits to each decision without later reconsideration.
## Inductive Bias:
The inductive bias of ID3 is a **preference bias** (also called a search bias). This means that while its hypothesis space is complete (it can represent any possible discrete-valued function), its search strategy leads it to prefer certain hypotheses over others. Specifically, ID3 prefers shorter trees over more complex ones and favors trees that place attributes with high information gain closer to the root of the tree.