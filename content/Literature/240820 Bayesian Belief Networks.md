---
title: Bayesian Belief Networks
draft: false
tags:
---
Are a representation of the probability of variables and their conditional dependencies through a graphical network. 

Where, 
- **Node:** Variable and it's associated Probability distribution. 
- **Parent Node:** Prior. 
- **Child Node:** Conditional Dependency. 

![[../Files/Pasted image 20240820112047.png|center|425]]

$$
\mathrm{P}(e)=\sum_{d \in \mathcal{D}} \mathrm{P}(e \mid d) \cdot \underbrace{\sum_{c \in \mathcal{C}} \sum_{a \in \mathcal{A}} \mathrm{P}(d \mid c, a) \cdot \mathrm{P}(a) \cdot \overbrace{\sum_{b \in \mathcal{B}} \mathrm{P}(c \mid b) \cdot \mathrm{P}(b)}^{\mathrm{P}(c)}}_{\mathrm{P}(d)}
$$
1. **Node A:** $P(a)$
2. **Node B:** $P(b)$
3. **Node C:** $P(c) = \sum_{b \in B} P(c|b) \cdot P(b)$
4. **Node D:** $P(d) = \sum_{a \in A} \sum_{c \in C} P(d|a,c) \cdot P(a) \cdot P(c)$
5. **Node E:** $P(e) = \sum_{d \in D} P(e|d) \cdot P(d)$

## Applications
- **Medical Diagnosis:** It can be used to model relationships between symptoms, diseases and risk factors. 
```mermaid
graph TD
    %% Patient Characteristics
    C1[Age]
    C2[Gender]
    C3[Family History]

    %% Diseases
    D1[Heart Disease]
    D2[Diabetes]
    D3[Hypertension]

    %% Symptoms
    S1[Chest Pain]
    S2[Shortness of Breath]
    S3[Fatigue]
    S4[Frequent Urination]

    %% Patient Characteristics to Diseases
    C1 --> D1 & D2 & D3
    C2 --> D1 & D2 & D3
    C3 --> D1 & D2 & D3

    %% Diseases to Symptoms
    D1 --> S1 & S2 & S3
    D2 --> S3 & S4
    D3 --> S2 & S3

    %% Styling
    classDef characteristics fill:stroke-width:2px;
    classDef diseases fill:stroke-width:2px;
    classDef symptoms fill:stroke-width:2px;

    class C1,C2,C3 characteristics;
    class D1,D2,D3 diseases;
    class S1,S2,S3,S4 symptoms;

    %% Title
    title[Medical Diagnosis Bayesian Network]
    style title fill:none,stroke:none
```