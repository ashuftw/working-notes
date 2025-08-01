---
title: Gaussian Mixture Regression (GMR)
draft: false
tags: 
date:
---
## Using GMM for Regression
Gaussian Mixture Regression (GMR) uses a [[250727 Gaussian Mixture Model|GMM]] to perform [[230418 Regression|Regression]]. The process is:
1.  **Model the Joint Space**: Combine the input and output data into a single vector, $z=(y,x)$. Train a GMM on this joint data space to learn the distribution $p(z)$.
2.  **Conditioning**: For a new input query $x_q$, calculate the conditional probability distribution $p(y|x_q)$ from the learned joint GMM. This conditional distribution is itself a Gaussian.
3.  **Predict**: The regression output for $x_q$ is the [[230505 Expected Value|expected value]] (mean) of this conditional distribution. The analytical solution for the predicted mean $\bar{y}$ is:
    $$\overline{y} = \sum_{e=1}^{E} h_e(x) (\mu_{e,Y} + \Sigma_{e,YX}\Sigma_{e,X}^{-1}(x - \mu_{e,X}))$$
    where $h_e(x)$ are weights corresponding to the responsibilities.

GMR has the same mathematical form as [[250711 Relating Models to the Unified Model|Locally Weighted Regression (LWR)]] and is considered a special case of a broader [[250701 Unified Model|unified model]] for regression. The unified model is expressed as:
$$t(x) = \sum_{e=1}^{E} \phi_c(x, \theta_e) (w_e^T x + b_e)$$
GMR fits into this framework, demonstrating its connection to a wide family of regression algorithms, including those based on mixtures of linear models and weighted sums of basis functions.