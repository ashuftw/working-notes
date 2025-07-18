## 2️⃣ Differential Equations (ALWAYS 20 points)

### Basic ODE Setup

```python
from scipy.integrate import solve_ivp

def ode_system(t, y, *args):
    """
    y = [state1, state2, ...]
    dydt = [dstate1/dt, dstate2/dt, ...]
    """
    # Unpack states
    x1, v1, x2, v2 = y
    
    # Parameters (can be passed via args)
    m1, m2, k1, k2, d1, d2 = args
    
    # Derivatives
    dx1dt = v1
    dv1dt = (-k1*x1 - d1*v1 + k2*(x2-x1) + d2*(v2-v1)) / m1
    dx2dt = v2
    dv2dt = (-k2*(x2-x1) - d2*(v2-v1)) / m2
    
    return [dx1dt, dv1dt, dx2dt, dv2dt]

# Initial conditions
y0 = [0, 0, 5, 0]  # [x1, v1, x2, v2]

# Time span
t_span = (0, 250)
t_eval = np.linspace(0, 250, 1000)

# Parameters
params = (3, 1, 1, 0.1, 0.01, 0.05)  # m1, m2, k1, k2, d1, d2

# Solve
sol = solve_ivp(ode_system, t_span, y0, 
                t_eval=t_eval, args=params,
                method='RK45')  # or 'Radau' for stiff

# Extract results
x1 = sol.y[0]
v1 = sol.y[1]
x2 = sol.y[2]
v2 = sol.y[3]
```

### Common ODE Templates

#### Spring-Mass-Damper

```python
def spring_mass_damper(t, y, m, k, d, F0=0, omega=0):
    x, v = y
    dxdt = v
    dvdt = (F0*np.sin(omega*t) - k*x - d*v) / m
    return [dxdt, dvdt]
```

#### Predator-Prey

```python
def predator_prey(t, y, a, b, c, d):
    H, F = y  # Prey (H), Predator (F)
    dHdt = a*H - b*F*H
    dFdt = -c*F + d*H*F
    return [dHdt, dFdt]
```

#### Chemical Reaction (Resin Curing)

```python
def resin_curing(t, y, A1, E1, m, n, R, Qm, cp, Qs):
    alpha, T = y  # Degree of cure, Temperature
    dalphadt = A1 * np.exp(-E1/(R*T)) * alpha**m * (1-alpha)**n
    dTdt = (Qm * dalphadt + Qs) / cp
    return [dalphadt, dTdt]
```

#### Electrical Circuit

```python
def rlc_circuit(t, y, R, L, C, V0, f):
    I, dIdt = y
    omega = 2 * np.pi * f
    V = V0 * np.sin(omega * t)
    d2Idt2 = (omega * V0 * np.cos(omega * t) - R*dIdt - I/C) / L
    return [dIdt, d2Idt2]
```

### Parameter Studies

```python
# Vary parameter and collect results
param_values = np.linspace(0.01, 0.1, 10)
final_values = []

for param in param_values:
    sol = solve_ivp(ode_system, t_span, y0, 
                    args=(param, other_params...))
    final_values.append(sol.y[:, -1])  # Last values

plt.plot(param_values, final_values, 'x--')
```