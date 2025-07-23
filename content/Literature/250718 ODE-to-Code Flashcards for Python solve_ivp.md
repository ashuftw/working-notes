---
title: ODE-to-Code Flashcards for Python solve_ivp
draft: true
tags: 
date: 2025-07-18
---
## Flashcard 1: Simple Exponential Decay

**Front:** First-order decay equation: 
$$
\frac{dy}{dt} = -ky
$$
 where k = 0.5 (decay constant)

**Back:**

```python
def ode_system(t, y):
    k = 0.5
    dydt = -k * y
    return dydt
```

---

## Flashcard 2: First-Order with Time-Dependent Input

**Front:** RC circuit with time-varying voltage: 
$$
\frac{dV_c}{dt} = \frac{1}{RC}(V_{in}(t) - V_c)
$$
 where R = 1000 Ω, C = 0.001 F, and $V_{in}(t) = 10\sin(2\pi t)$

**Back:**

```python
def ode_system(t, y):
    R = 1000
    C = 0.001
    V_in = 10 * np.sin(2 * np.pi * t)
    
    dVc_dt = (1/(R*C)) * (V_in - y[0])
    return [dVc_dt]
```

---

## Flashcard 3: Second-Order to First-Order System

**Front:** Mass-spring system: 
$$
m\ddot{x} + c\dot{x} + kx = 0
$$
 where m = 2 kg, c = 0.5 N·s/m, k = 10 N/m

**Back:**

```python
def ode_system(t, y):
    # y[0] = x (position)
    # y[1] = x_dot (velocity)
    m = 2
    c = 0.5
    k = 10
    
    x = y[0]
    x_dot = y[1]
    
    x_ddot = (-c*x_dot - k*x) / m
    
    return [x_dot, x_ddot]
```

---

## Flashcard 4: Coupled First-Order System

**Front:** Predator-prey (Lotka-Volterra) model: 
$$
\frac{dx}{dt} = ax - bxy
$$
 
$$
\frac{dy}{dt} = -cy + dxy
$$
 where a = 1.5, b = 0.1, c = 0.75, d = 0.02

**Back:**

```python
def ode_system(t, y):
    # y[0] = x (prey population)
    # y[1] = y (predator population)
    a = 1.5
    b = 0.1
    c = 0.75
    d = 0.02
    
    x = y[0]
    pred = y[1]
    
    dx_dt = a*x - b*x*pred
    dy_dt = -c*pred + d*x*pred
    
    return [dx_dt, dy_dt]
```

---

## Flashcard 5: Forced Oscillator with Damping

**Front:** Driven harmonic oscillator: 
$$
m\ddot{x} + c\dot{x} + kx = F_0\cos(\omega t)
$$
 where m = 1 kg, c = 0.2 N·s/m, k = 4 N/m, F₀ = 2 N, ω = 3 rad/s

**Back:**

```python
def ode_system(t, y):
    # y[0] = x (position)
    # y[1] = x_dot (velocity)
    m = 1
    c = 0.2
    k = 4
    F0 = 2
    omega = 3
    
    x = y[0]
    x_dot = y[1]
    
    F_ext = F0 * np.cos(omega * t)
    x_ddot = (F_ext - c*x_dot - k*x) / m
    
    return [x_dot, x_ddot]
```

---

## Flashcard 6: RLC Circuit

**Front:** Series RLC circuit: 
$$
L\frac{d^2q}{dt^2} + R\frac{dq}{dt} + \frac{q}{C} = V_0
$$
 where L = 0.1 H, R = 20 Ω, C = 0.0001 F, V₀ = 12 V

**Back:**

```python
def ode_system(t, y):
    # y[0] = q (charge)
    # y[1] = i (current = dq/dt)
    L = 0.1
    R = 20
    C = 0.0001
    V0 = 12
    
    q = y[0]
    i = y[1]
    
    di_dt = (V0 - R*i - q/C) / L
    
    return [i, di_dt]
```

---

## Flashcard 7: Double Pendulum (Small Angle Approximation)

**Front:** Linearized double pendulum: 
$$
\ddot{\theta_1} = -\frac{g(m_1 + m_2)}{m_1 l_1}\theta_1 + \frac{m_2 g}{m_1 l_1}\theta_2
$$
 
$$
\ddot{\theta_2} = \frac{g}{l_2}\theta_1 - \frac{g}{l_2}\theta_2
$$
 where g = 9.81 m/s², m₁ = m₂ = 1 kg, l₁ = l₂ = 1 m

**Back:**

```python
def ode_system(t, y):
    # y[0] = theta1, y[1] = theta1_dot
    # y[2] = theta2, y[3] = theta2_dot
    g = 9.81
    m1 = m2 = 1
    l1 = l2 = 1
    
    theta1 = y[0]
    theta1_dot = y[1]
    theta2 = y[2]
    theta2_dot = y[3]
    
    theta1_ddot = -g*(m1 + m2)/(m1*l1)*theta1 + m2*g/(m1*l1)*theta2
    theta2_ddot = g/l2*theta1 - g/l2*theta2
    
    return [theta1_dot, theta1_ddot, theta2_dot, theta2_ddot]
```

---

## Flashcard 8: Van der Pol Oscillator

**Front:** Van der Pol equation: 
$$
\ddot{x} - \mu(1 - x^2)\dot{x} + x = 0
$$
 where μ = 1.5 (nonlinearity parameter)

**Back:**

```python
def ode_system(t, y):
    # y[0] = x
    # y[1] = x_dot
    mu = 1.5
    
    x = y[0]
    x_dot = y[1]
    
    x_ddot = mu*(1 - x**2)*x_dot - x
    
    return [x_dot, x_ddot]
```

---

## Flashcard 9: Coupled Spring-Mass System

**Front:** Two masses connected by springs: 
$$
m_1\ddot{x_1} = -k_1x_1 + k_2(x_2 - x_1)
$$
 
$$
m_2\ddot{x_2} = -k_2(x_2 - x_1) - k_3x_2
$$
 where m₁ = 2 kg, m₂ = 1 kg, k₁ = 100 N/m, k₂ = 50 N/m, k₃ = 75 N/m

**Back:**

```python
def ode_system(t, y):
    # y[0] = x1, y[1] = x1_dot
    # y[2] = x2, y[3] = x2_dot
    m1 = 2
    m2 = 1
    k1 = 100
    k2 = 50
    k3 = 75
    
    x1 = y[0]
    x1_dot = y[1]
    x2 = y[2]
    x2_dot = y[3]
    
    x1_ddot = (-k1*x1 + k2*(x2 - x1)) / m1
    x2_ddot = (-k2*(x2 - x1) - k3*x2) / m2
    
    return [x1_dot, x1_ddot, x2_dot, x2_ddot]
```

---

## Flashcard 10: SIR Epidemic Model

**Front:** SIR model for disease spread: 
$$
\frac{dS}{dt} = -\beta SI
$$
 
$$
\frac{dI}{dt} = \beta SI - \gamma I
$$
 
$$
\frac{dR}{dt} = \gamma I
$$
 where β = 0.0005 (transmission rate), γ = 0.1 (recovery rate)

**Back:**

```python
def ode_system(t, y):
    # y[0] = S (susceptible)
    # y[1] = I (infected)
    # y[2] = R (recovered)
    beta = 0.0005
    gamma = 0.1
    
    S = y[0]
    I = y[1]
    R = y[2]
    
    dS_dt = -beta * S * I
    dI_dt = beta * S * I - gamma * I
    dR_dt = gamma * I
    
    return [dS_dt, dI_dt, dR_dt]
```

---

## Flashcard 11: Nonlinear Chemical Reaction

**Front:** Brusselator model: 
$$
\frac{dx}{dt} = a + x^2y - bx - x
$$
 
$$
\frac{dy}{dt} = bx - x^2y
$$
 where a = 1, b = 3

**Back:**

```python
def ode_system(t, y):
    # y[0] = x (concentration of species X)
    # y[1] = y (concentration of species Y)
    a = 1
    b = 3
    
    x = y[0]
    conc_y = y[1]
    
    dx_dt = a + x**2 * conc_y - b*x - x
    dy_dt = b*x - x**2 * conc_y
    
    return [dx_dt, dy_dt]
```

---

## Flashcard 12: Rigid Body Rotation (Euler's Equations)

**Front:** Euler's equations for rigid body rotation: 
$$
I_1\dot{\omega_1} = (I_2 - I_3)\omega_2\omega_3 + M_1
$$
 
$$
I_2\dot{\omega_2} = (I_3 - I_1)\omega_3\omega_1 + M_2
$$
 
$$
I_3\dot{\omega_3} = (I_1 - I_2)\omega_1\omega_2 + M_3
$$
 where I₁ = 2, I₂ = 3, I₃ = 4 kg·m², and M₁ = M₂ = M₃ = 0 (no external torques)

**Back:**

```python
def ode_system(t, y):
    # y[0] = omega1, y[1] = omega2, y[2] = omega3
    I1 = 2
    I2 = 3
    I3 = 4
    M1 = M2 = M3 = 0
    
    omega1 = y[0]
    omega2 = y[1]
    omega3 = y[2]
    
    omega1_dot = ((I2 - I3)*omega2*omega3 + M1) / I1
    omega2_dot = ((I3 - I1)*omega3*omega1 + M2) / I2
    omega3_dot = ((I1 - I2)*omega1*omega2 + M3) / I3
    
    return [omega1_dot, omega2_dot, omega3_dot]
```