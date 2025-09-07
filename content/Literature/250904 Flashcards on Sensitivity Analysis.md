---
title: Flashcards on Sensitivity Analysis
draft: true
tags:
date: 2025-09-04
---
### What is the primary goal of Sensitivity Analysis in the context of Uncertainty Quantification? Name its two main practical applications.

The primary goal of Sensitivity analysis is to examine which model input parameters are most influential from an uncertainty perspective. More precisely, the aim is to identify those parameters, which if they are uncertain, contribute most to the output variance.

The two main applications are:
1.  **Parameter Prioritization**: Identifying the most influential inputs, so efforts to reduce uncertainty (e.g., through more accurate measurements) can be focused where they matter most.
2.  **Parameter Fixing**: Identifying non-influential inputs that can be fixed to their nominal values, simplifying the model without significantly affecting the output uncertainty.

---
### What is the fundamental limitation of **Local Sensitivity Analysis** methods like the "one-at-a-time" (OAT) approach?

**Back:**
The fundamental limitation is that it **neglects interaction effects** between input variables.

OAT analyzes the effect of changing one input while holding all others constant at their nominal values. It cannot capture scenarios where the influence of one variable depends on the value of another.

---
### What is the core difference between Local and Global Sensitivity Analysis?

The core difference is that **Local SA** analyzes the impact of changing one input at a time around a single nominal point, while **Global SA** analyzes the impact of all inputs varying simultaneously across their entire ranges of uncertainty.

| Feature             | Local SA (e.g., OAT)                                                | Global SA (e.g., Sobol')                                    |
| :------------------ | :------------------------------------------------------------------ | :---------------------------------------------------------- |
| **Input Variation** | Varies one input at a time. (the other is fixed at a nominal point) | Varies all inputs simultaneously.                           |
| **Scope**           | Explores the model's response around a single **nominal point**.    | Explores the entire input parameter space.                  |
| **Interactions**    | **Ignores** interaction effects between inputs.                     | **Quantifies** both direct effects and interaction effects. |
| **Typical Output**  | Local derivatives or a "Tornado Plot".                              | Variance-based measures like Sobol' Indices.                |

**In short:** Local SA is like checking the slope at one specific spot on a hill, while Global SA describes the influence of each dimension on the entire landscape.

---
### What is the key difference between how OAT and the First-order Sobol index  isolate a variable's main effect?
The key difference is how they treat the other input variables:
-   **OAT (Local):** Varies one input while all other inputs are **FIXED** at a single nominal point. Its result is only valid locally.
-   **$S_i$ (Global):** Measures one input's effect by **AVERAGING** its influence over the entire distribution of all other inputs. Its result is globally valid.

| Method    | How it treats other inputs         | Scope of Result |
| :-------- | :--------------------------------- | :-------------- |
| **OAT**   | **Fixed** at a nominal point       | **Local**       |
| **$S_i$** | **Averaged** over their full range | **Global**      |

--- 
### What is the theoretical foundation of variance-based Global Sensitivity Analysis (GSA), and what is the name of the resulting decomposition?

The foundation is the **Hoeffding decomposition** (also called High-Dimensional Model Representation or HDMR), which uniquely represents any square-integrable function as a sum of functions of increasing dimensionality.

When applied to the variance of a model's output, this results in the **ANOVA (Analysis of Variance) decomposition**.

---

#### What is the **Total Effect Index ($S_{T_i}$)**, and how does comparing it to the first-order index ($S_i$) reveal information about a parameter's behavior?

The **Total Effect Index ($S_{T_i}$)** measures the contribution of an input variable $X_i$ to the output variance, including its direct effect **and** all of its interaction effects with other variables.

-   If $S_{T_i} \approx S_i$, the parameter $X_i$ acts mostly independently.
-   If $S_{T_i} > S_i$, the parameter $X_i$ is involved in significant interaction effects with other parameters.
-   If $S_{T_i} \approx 0$, the parameter can be fixed (is non-influential).

---

#### How can a **Polynomial Chaos Expansion (gPC)** be used to efficiently calculate Sobol' Indices without running new model simulations?

Once a gPC surrogate model is constructed, the Sobol' indices can be calculated **directly and analytically from the gPC coefficients**.

The total variance and the partial variances ($D_A$) have simple closed-form expressions based on sums of the squares of the coefficients. This avoids the high computational cost of the Monte Carlo methods typically used to estimate the indices.

---

#### How does Sensitivity Analysis guide the use of other UQ methods, such as **anisotropic Quadrature**?

Sensitivity Analysis identifies the most influential input parameters. This knowledge is crucial for building efficient **anisotropic** UQ models.

For example, when setting up an anisotropic quadrature grid, you can assign more quadrature points (higher resolution) to the dimensions identified by GSA as most influential and fewer points to the unimportant dimensions. This focuses computational effort where it is most needed, mitigating the curse of dimensionality.