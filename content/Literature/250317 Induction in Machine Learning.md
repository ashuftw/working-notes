---
title: Induction in Machine Learning
draft: false
tags: 
date: 2025-03-17
---
## Inductive Learning Hypothesis
Any hypothesis that can approximate the target function well over a sufficiently large set of training examples can also approximate the target function well over other unobserved examples.
## **Learning Bias** (or Inductive Bias)
This refers to the set of assumptions a learning algorithm makes to predict outputs for new inputs i.e it is "a set of arbitrary assumptions" that enable the learner to generalize.
Two main types of bias
- **Restriction bias:** Limiting the hypothesis space (as in Candidate Elimination)
- **Preference bias:** Preferring certain hypotheses over others (as in ID3's greedy search)