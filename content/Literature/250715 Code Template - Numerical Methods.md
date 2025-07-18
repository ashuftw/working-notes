## 4️⃣ Numerical Methods (OCCASIONAL 10-15 points)

### Root Finding

```python
from scipy.optimize import newton, fsolve

# Single equation
def equation(x, rd=0.05):
    return 3*x - 4*x**3 - rd

# Find root
x_solution = newton(equation, x0=0.1, args=(0.05,))

# System of equations
def system(vars):
    x, y = vars
    eq1 = x**2 + y**2 - 1
    eq2 = x - y
    return [eq1, eq2]

solution = fsolve(system, [0.5, 0.5])
```

### Linear Systems

```python
# Solve Ax = b
A = np.array([[1, 2], [3, 4]])
b = np.array([5, 6])
x = np.linalg.solve(A, b)
```

### Integration

```python
from scipy.integrate import quad

def integrand(x):
    return x**2 * np.exp(-x)

result, error = quad(integrand, 0, np.inf)
```