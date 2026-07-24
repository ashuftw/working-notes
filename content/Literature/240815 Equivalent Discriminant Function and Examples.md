---
title: Equivalent Discriminant Function and Examples
draft: false
date: 2024-08-15
---

The Discriminant function can be modified without changing the classification outcome. 
- **Scaling by a positive constant**


	$$
	g_i(x) \rightarrow \alpha g_i(x), \alpha > 0
	$$


- **Adding a constant**


	$$
	g_i(x) \rightarrow \alpha + g_i(x), \alpha \in \mathbb{R}
	$$


- **Applying a function**


	$$
	g_i(\mathbf{x}) \rightarrow f\left(g_i(\mathbf{x})\right)
	$$


These transformations are often used to simplify the mathematical calculations involved in classification. Where $f(\cdot)$ is a monotonically increasing function
## Use cases 
- Improving the confidence of the decision by having a very high $\alpha$
- Using $\alpha$ in the context of a multi-class problem to normalize each classification. 
## Q 
**How can you simplify a discriminant function without changing the classification result?**

---

