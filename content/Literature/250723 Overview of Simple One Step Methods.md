---
title: Overview of Simple One Step Methods
draft: false
tags: 
date: 2025-07-23
---
### Euler methods
**Explicit**
$$
y_{i+1} = y_i + h_i f(t_i, y_i)
$$
**Implicit**
$$
y_{i+1} = y_i + h_i f(t_{i+1}, y_{i+1})
$$
### Crank-Nicolson method

$$
y_{i+1} = y_i + \frac{h_i}{2}[f(t_i, y_i) + f(t_{i+1}, y_{i+1})]
$$

### Euler-Heun Method

$$
y_{i+1} = y_i + \frac{h_i}{2}[f(t_i, y_i) + f(t_{i+1}, y_i + h_i f(t_i, y_i))]
$$

### Improved Euler Method

$$
y_{i+1} = y_i + h_i f\left(t_i + \frac{h_i}{2}, y_i + \frac{h_i}{2}f(t_i, y_i)\right)
$$

### Classical Runge-Kutta Method

$$
\begin{align*}
q_1 &= hf(t_i, y_i) \\
q_2 &= hf\left(t_i + \frac{h}{2}, y_i + \frac{1}{2}q_1\right) \\
q_3 &= hf\left(t_i + \frac{h}{2}, y_i + \frac{1}{2}q_2\right) \\
q_4 &= hf(t_i + h, y_i + q_3) \\
y_{i+1} &= y_i + \frac{1}{6}(q_1 + 2q_2 + 2q_3 + q_4)
\end{align*}
$$