---
title: Separating Variables
draft: false
date: 2022-11-08
---

If there exists differential equation such that

$$
\frac{dy}{dt}=y\prime=f(y,t)=h(y)\cdot g(t)
$$

Then by Separation of Variables we have 

$$
\frac{1}{h(y)}dy=g(t)dt
$$

Now it's possible to integrate them

$$
\int\frac{1}{h(y)}dy=\int g(t)dt+c
$$

We have added the constant of integration at the time of integration to indicate the ambiguity, that is dependant on the initial conditions. 
Since we are integrating functions (implicit) it is good practice to add the $c$ before hand. 

**Examples
1. $y\prime = \dfrac{2y}{t}$
	
$$
\begin{aligned}
	\frac{dy}{dt} &= 2y \cdot \frac{1}{t}\\
	\frac{1}{2y}dy&=\frac{1}{t}dt\\
	\int \frac{1}{2y}dy&=\int \frac{1}{t}dt+c
	\
	\end{aligned}
$$

