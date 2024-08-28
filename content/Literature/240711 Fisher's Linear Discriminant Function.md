---
title: Fisher's Linear Discriminant Function
draft: false
tags:
---
  
## Motivation
We try to find a weight vector $\mathbf w$ such that the Hyper Plane is $\bot$ to it.     

![[../../Private/Excalidraw/Drawing 2024-07-11 12.24.02.excalidraw#^area=hp6QKA36ghicwuo8VO50m|center]]
The position of the Hyper Plane however is not known. We can find it using the following methods.
## Approach 1: Maximize the inter-class variance
Maximise the distance between the projected means. In simple terms we try to find $\mathbf w$ that has the greatest distance between the projected means. 
**Mathematically**

$$
\begin{aligned}
\max _{\mathbf{w}}\left|m_1^{\prime}-m_2^{\prime}\right|&\Leftrightarrow \max _{\mathbf{w}}\left|\mathbf{w}^T \mathbf{m}_1-\mathbf{w}^T \mathbf{m}_2\right|\\
&=\max _{\mathbf{w}}\left|\mathbf{w}^T( \mathbf{m}_1-\mathbf{m}_2)\right|
\end{aligned}
$$

Hence, 

$$
\mathbf{w} \propto\left(\mathbf{m}_2-\mathbf{m}_1\right)
$$

$\mathbf w$ points in the same direction as $(\mathbf{m}_2-\mathbf{m}_1)$



