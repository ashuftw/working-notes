---
title: Overview of Uncertainty Quantification
draft: true
tags:
date: 2025-09-01
---

### Core Goal: Uncertainty Quantification (UQ)
The **Core Goal** of **UQ** is to understand how **input** uncertainty ***propagates*** through a model to create **output** uncertainty. 
or
The **Core Goal** of **UQ** is to understand how uncertainty in the **inputs** of a mathematical model ***propagates*** through it to create uncertainty in the **outputs**.

Everything revolves around the abstract model representation:

$$
y = \mathcal{M}(x)
$$

- $x$: The vector of **uncertain model inputs** (e.g., material properties, loads, geometric parameters).
- $\mathcal{M}$: The **mathematical model** itself, which can be a simple function or a complex simulation like a Finite Element (FE) analysis.
- $y$: The **uncertain model output**, or "quantity of interest".

---

### The Foundation: Modeling Uncertainty

Before we can propagate uncertainty, we need a mathematical language to describe it. This is the role of probability theory.

* **Random Variables**: Used to model single uncertain parameters like a damping ratio ($\zeta$) or natural frequency ($\omega_n$).
    * They are described by **Probability Density Functions (PDFs)**, such as Normal (Gaussian), Log-Normal, or Uniform distributions.
* **Random Vectors**: Used to model multiple uncertain parameters at once, which may be correlated. The relationship between variables is captured by the **covariance matrix**.
* **Random Processes & Fields**: Used when uncertainty is distributed over time or space, like an uncertain load $q(r)$ on a beam.
    * **Karhunen-Loève (KL) Expansion**: A key technique to represent a complex random field with a series of uncorrelated random variables ($\xi_i$), which are easier to work with. This is often a crucial first step before applying other UQ methods.

---

### The Main Task: Propagating Uncertainty

Once the inputs are described as random variables, the goal is to determine the resulting probability distribution of the output $y$. This typically means finding its moments (mean, variance), its PDF, or its Cumulative Distribution Function (CDF). The main challenge is that running the model $\mathcal{M}$ can be extremely slow and computationally expensive.

The methods to solve this problem fall into three main categories:

#### 1. Simplified Analytical Methods

These are quick but often less accurate, best suited for simple problems or initial estimates.

* **First-Order Second-Moment (FOSM) Method**:
    * **How it works**: Approximates the model $\mathcal{M}$ with a simple linear Taylor expansion around the mean value of the inputs.
    * **Result**: Gives a rough estimate of the output mean and variance.
    * **Limitation**: Only accurate when input uncertainties are very small and the model is nearly linear.

#### 2. Surrogate Modeling Methods

The core idea is to replace the expensive model $\mathcal{M}$ with a cheap, fast-to-evaluate approximation called a **surrogate model** ($\tilde{\mathcal{M}}$).

* **Polynomial Chaos (PC) Expansion**:
    * **How it works**: Represents the model output as a weighted sum of special **orthogonal polynomials** of the input random variables: $Y \approx \sum q_i \Phi_i(X)$. The type of polynomial (e.g., Hermite for Gaussian inputs, Legendre for Uniform inputs) is matched to the input's PDF.
    * **Finding the Coefficients ($q_i$)**:
        * **Non-Intrusive Projection**: Treats the model as a "black box." It runs the full model $\mathcal{M}$ at a few smart points (**quadrature nodes**) and uses the results to calculate the coefficients. This is flexible but may require many model runs.
        * **Intrusive (Stochastic Galerkin) Method**: Modifies the underlying equations of the model (e.g., the FE formulation) to solve for the PC coefficients directly. This is very efficient but requires access to and modification of the model's source code.
    * **Result**: A fast surrogate model. Once you have the coefficients, you can instantly calculate the output's **mean** ($q_0$) and **variance** ($\sum q_i^2$) and run millions of virtual experiments for free.

#### 3. Sampling-Based Methods

These methods rely on running the original model $\mathcal{M}$ many times for different random inputs.

* **Monte Carlo (MC) Method**:
    * **How it works**: The most direct approach. Simply generate thousands of random input samples, run the model for each one, and compute the average and variance of the outputs.
    * **Advantage**: It always works, regardless of model complexity, and doesn't suffer from the "curse of dimensionality".
    * **Limitation**: Very slow convergence. The error decreases with $1/\sqrt{K}$ (where K is the number of samples), so it can be computationally infeasible for expensive models.
* **Advanced MC (Variance Reduction)**: Techniques to get better accuracy with fewer model runs.
    * **Control Variates**: Uses a cheap approximate model (like a surrogate or a simplified physical model) to correct the standard MC estimate, reducing the overall variance.
    * **Multilevel Monte Carlo (MLMC)**: Used when the model can be run at different fidelity levels (e.g., coarse and fine FE meshes). It performs most of the simulations on cheap, low-fidelity models and only a few expensive, high-fidelity simulations for correction.

---

### The Analysis: Interpreting the Results

After propagating uncertainty, we can analyze the output to gain deeper insights.

* **Sensitivity Analysis**:
    * **Goal**: To determine which input parameters are most responsible for the uncertainty in the output.
    * **Sobol Indices**: A powerful technique that decomposes the total output variance into parts attributable to each input individually ($S_i$) and to their interactions ($S_{ij}$). This tells you exactly where the uncertainty is coming from.
        * These indices can be calculated very efficiently if you already have a **Polynomial Chaos** surrogate model.