---
title: Important Concepts
draft: true
tags: 
date: 2025-08-14
---
## ▶▶ The EM Algorithm (Slides 101, 102, 103, 105)

### Core Concept:

The **Expectation-Maximization (EM) algorithm** is an iterative method for finding Maximum Likelihood (ML) estimates of parameters in a statistical model when the model depends on unobserved, latent variables. It's particularly useful for training Gaussian Mixture Models (GMMs).

The algorithm guarantees that the log-likelihood will increase with each iteration, converging to a local maximum.

### The Two Steps:

The EM algorithm alternates between two key steps:
1. **E-step (Expectation):** It computes an expectation of the log-likelihood, using the current parameter estimates. This involves calculating the posterior probabilities (responsibilities) of each data point belonging to each component.
2. **M-step (Maximization):** It re-estimates the parameters (weights, means, covariances) by maximizing the expected log-likelihood found in the E-step.

### Flashcard Questions:
* **What problem does the EM algorithm solve?**
    * It finds Maximum Likelihood parameter estimates for models with unobserved latent variables, like GMMs.
* **What are the two steps of the EM algorithm?**
    * Expectation (E-step) and Maximization (M-step).
* **What is the goal of the E-step?**
    * To compute the expectation of the log-likelihood based on current parameters.
* **What is the goal of the M-step?**
    * To update the model's parameters to maximize the expected log-likelihood.
* **Is the EM algorithm guaranteed to find the global optimum?**
    * No, it's guaranteed to converge to a local maximum.

---
## ▶ Support Vector Machines (SVMs) (Slides 161-188)

### Core Concept:

**Support Vector Machines (SVMs)** are powerful supervised learning models used for classification. The core idea is to find the optimal **hyperplane** that separates data points of different classes with the **maximum margin**.

* **Margin:** The distance between the decision hyperplane and the nearest data points from either class. Maximizing the margin improves the model's generalization to new, unseen data.
* **Support Vectors:** These are the data points that lie closest to the decision boundary. They are the most critical elements of the training set because they are the ones that "support" or define the hyperplane. If you remove any other data point, the hyperplane will not change.

### The Kernel Trick:

SVMs can handle non-linearly separable data by using the **kernel trick**. This involves mapping the original data into a higher-dimensional space where it becomes linearly separable. This is done without ever explicitly computing the coordinates of the data in this new space, which would be computationally expensive. Instead, it uses a **kernel function** to compute the inner products between the images of all pairs of data in the feature space.

### The Relaxed (Soft-Margin) Case:

In real-world scenarios, data is often not perfectly separable. The **soft-margin** SVM allows for some misclassifications by introducing **slack variables** ($\xi$). These variables allow some data points to be on the wrong side of the margin, or even on the wrong side of the hyperplane. A cost parameter, **C**, controls the trade-off between maximizing the margin and minimizing the classification error.

### Flashcard Questions:
* **What is the main goal of an SVM in classification?**
    * To find the hyperplane that separates classes with the maximum possible margin.
* **What are support vectors?**
    * The training data points closest to the decision hyperplane that define its position.
* **What is the "kernel trick"?**
    * A method to handle non-linearly separable data by mapping it to a higher dimension using a kernel function, without explicitly computing the transformation.
* **What problem does a soft-margin SVM solve?**
    * It allows SVMs to handle non-separable data by permitting some misclassifications, controlled by a cost parameter C.
* **What do slack variables ($\xi$) represent in a soft-margin SVM?**
    * They measure the degree of misclassification for each data point that is on the wrong side of the margin.

---
## ▶▶ Deep Learning & LSTMs (Slides 104, 106-109, and concepts throughout the SVM/NN sections)

### The Vanishing Gradient Problem:

Training deep neural networks and standard RNNs is challenging due to the **vanishing gradient problem**. During backpropagation, the error gradient can become exponentially smaller as it flows backward from the output to the initial layers. This means the early layers learn very slowly or not at all, preventing the network from learning long-term dependencies.

### LSTM: The Solution for Sequences

**Long Short-Term Memory (LSTM)** networks are a type of RNN specifically designed to overcome this problem.

* **Core Component:** The **Constant Error Carousel (CEC)**. This is the "memory cell" of the LSTM, which allows information to flow through the network largely unchanged over long sequences.
* **Gating Mechanism:** LSTMs use three "gates" to control the flow of information into and out of the memory cell:
    1.  **Input Gate:** Decides what new information to store in the cell.
    2.  **Forget Gate:** Decides what information to discard from the cell.
    3.  **Output Gate:** Decides what information from the cell to use for the output at the current time step.

### Training LSTMs:

LSTMs are trained using **Backpropagation Through Time (BPTT)**. The network is "unfolded" over time, creating a deep feedforward network, and then standard backpropagation is applied. The CEC ensures that the error gradient can flow back through many time steps without vanishing.

### Flashcard Questions:
* **What is the vanishing gradient problem?**
    * The issue where the error gradient shrinks exponentially as it is backpropagated, preventing early layers from learning.
* **What is the core component of an LSTM that solves this problem?**
    * The Constant Error Carousel (CEC) or memory cell.
* **What are the three gates in an LSTM and what do they do?**
    * **Input Gate** (stores new info), **Forget Gate** (discards old info), and **Output Gate** (uses info for output).
* **How are LSTMs trained?**
    * Using Backpropagation Through Time (BPTT), where the network is unfolded over time.