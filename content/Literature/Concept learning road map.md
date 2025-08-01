---
title: Concept learning road map
draft: true
tags: 
date:
---
### Tier 1: Highest Priority (Must-Know)

These questions cover the absolute fundamental and most emphasized concepts in the lectures. You should be very comfortable with these.

- **15. Please define the term information gain. How is it computed (write down in math terms).**
    
    - **Why:** This is the core mechanism of the ID3 decision tree algorithm [1458, 1469]. The exam examples show that knowing and understanding key formulas is required. You'll need the formulas for Entropy (S) [1491] and Information Gain (ΔS) [1590].
        
- **17. How is the search organized for ID3 and what is the inductive bias?**
    
    - **Why:** This is a critical point of analysis. The search is "greedy" (it maximizes information gain at each step without looking ahead) [1616, 1669]. Its bias is a _preference bias_ for smaller trees, not a restriction on what it can represent [1670, 1698].
        
- **23. What is the naive Bayes classifier? How to estimate the respective terms?**
    
    - **Why:** This is the main practical algorithm from the Bayesian section. You need to know the classifier formula (y~​=argmaxyj​​∏ai​​P(ai​∣yj​)P(yj​)) [2095] and how to estimate the prior P(yj​) and likelihood P(ai​∣yj​) from frequencies in the training data [2089, 2093].
        
- **1. What is the goal of concept learning? Formalize the learning scenario.**
    
    - **Why:** It's the foundational question. The goal is to identify a subset of instances (the concept) by learning a boolean function from training examples [2662, 2673]. The formal scenario involves an instance space X, a target concept c, training examples D, and a hypothesis space H [2571, 2588, 2948].
        
- **18. What different types of inductive biases exist?**
    
    - **Why:** The slides explicitly contrast **restriction bias** (the hypothesis space is incomplete, e.g., Candidate-Elimination) with **preference bias** (the search is incomplete, e.g., ID3's greedy search) [1688, 1702, 1670, 1698]. This is a key comparative point.
        

---

### Tier 2: High Priority (Very Likely to Appear)

These questions cover other major topics and definitions that are central to the lectures.

- **9. What is a consistent hypothesis? What is the version space?**
    
    - **Why:** These are the core definitions for the Candidate-Elimination algorithm. A hypothesis is consistent if it correctly classifies all training examples [3981]. The version space is the set of all hypotheses consistent with the data [3981].
        
- **13. Describe the proceeding for decision trees.**
    
    - **Why:** You need to be able to explain how a tree classifies instances by starting at the root and moving down the branches based on attribute values [1225, 1233]. The key learning question is which attribute to pick at each node [1440].
        
- **19. Please compare decision trees and learning by generalization and specialization, specifically wrt. their biases.**
    
    - **Why:** This is a perfect exam-style synthesis question. Candidate-Elimination (generalization/specialization) uses a **restriction bias** by limiting the language of hypotheses [1688, 1702]. ID3 uses a **preference bias** by preferring smaller trees via its greedy search [1698, 1707].
        
- **24. Which assumption is used to derive the naive Bayes, why can this be problematic? Given an example!**
    
    - **Why:** The "naive" assumption is the conditional independence of attributes given the class [2092]. This is often violated in reality (e.g., in the surfing example, `month` and `temp` are likely related) and is a crucial limitation to understand.
        
- **22. What is the optimal Bayes classificator? Why is it problematic?**
    
    - **Why:** It provides the most probable classification by weighting the prediction of each hypothesis by its posterior probability [2013, 2031]. It's problematic because it's often computationally infeasible, requiring calculation over the entire hypothesis space [2061].
        
- **5. Please explain the “more general” relation and give examples.**
    
    - **Why:** This partial ordering (≥g​) is the structural backbone of the Version Space algorithm [3870, 3873]. Hypothesis h1​ is more general than h2​ if it classifies every instance that h2​ classifies as positive, and possibly more.
        

---

### Tier 3: Lower Priority (Good to Know)

These are more foundational or detailed questions. They are less likely to be major questions but are good for a complete understanding.

- **2. What is a concept? (Give different equivalent descriptions).**
    
- **4. Why is the application of hypotheses useful? Why is direct search in the space of concepts a bad idea?**
    
- **7. Give an example for what can not represented with this hypothesis space.** (For the attribute-value conjunctions, e.g. disjunctions).
    
- **8. How does search through generalization works? Please state problems.** (Find-S algorithm).
    
- **12. What’s about bias free learning? If it exists, is it useful?** (No, it's not useful as it can't generalize).
    
- **20. Give the Bayes-rule for hypothesis and name the terms.**
    
- **21. What can be said about consistent hypothesis and their probabilities from the Bayesian approach?**