---
title: Relationship between CDF and PDF
draft: false
tags: 
date: 2025-07-22
---
### In terms of areas
A [[230424 Cumulative Distribution Function (CDF)|CDF]] can be drawn from a  [[230424 Probability Density Function (PDF)|PDF]] as follows : 

![[../Files/cdf-pdf.png|center|750]]

Area accumulated by $f_X(\theta)$ up to point $c$ equals $F_X(c)$.

### Mathematically
The [[230424 Probability Density Function (PDF)|PDF]] is simply the derivative of the [[230424 Cumulative Distribution Function (CDF)|CDF]]: 
$$
f_X(x) = F_X'(x) = \frac{d}{dx}F_X(x)
$$

The CDF is then the integral of the PDF: 
$$
F_X(x) = \int_{-\infty}^{x} f_X(t) , dt
$$



