---
title: Code Template for Solving ODEs in Python
draft: false
tags: 
date: 2025-07-19
---
## Setup and Solving 

```python
from scipy.integrate import solve_ivp

def system(t, y,parameters):
    # y: state vector [y1, y2, ...], where y1=y[0], y2=y[1], etc.
	
    y1, y2 = y  # Unpack the state vector
    # Define the differential equations
    # dydt = [dy1/dt, dy2/dt, ...]
    dy1_dt = p1 * y1 - p2 * y1 * y2  # Example equation 1
    dy2_dt = p2 * y1 * y2 - p1 * y2  # Example equation 2
    
    return [dy1_dt, dy2_dt]

#sol = solve_ivp(system, [t0, tf], y0, args=(params,),method='RK45', dense_output=True)
t_span = [0, 600]
t_eval = np.linspace(t_span[0], t_span[1], 3000)
sol = solve_ivp(fun=system, t_span=t_span, y0=y0, t_eval=t_eval, args=(params,), method='RK45')

# sol.t -> array of time points
# sol.y -> array of solution values, where sol.y[0] is y1(t) and sol.y[1] is y2(t)
# t_eval = np.linspace(0, 0.3, 1000) if you want to specify steps
# y0 = [] has to be an array
```

## Parameterization 
```python
# --- Parametric Loop to Find the end values ---
final_values = [] # List to store the results
for param in parameter_list:
    # 1. Run the simulation for the current parameter
    sol = solve_ivp(system, [0, 100], y0,args=(param,), method='RK45')
    # 2. Extract the FINAL value of the first state variable and append it
    final_value = sol.y[0][-1]
    final_values.append(final_value)

# --- Parametric Loop to Find the Time to Reach a Value ---
threshold_value =  

times_to_threshold = [] # List to store the results
for param in parameter_list:
    # 1. Run the simulation for the current parameter
    # Note: Ensure the t_span is long enough for the threshold to be reached.
    sol = solve_ivp(system, [0, 500],y0, args=(param,), method='RK45')

    # 2. Find the time when the threshold is crossed
    try:
        # Find the first index where the state variable is >= the threshold
        index = np.where(sol.y[0] >= threshold_value)[0][0]
        # Get the corresponding time at that index
        time = sol.t[index]
        times_to_threshold.append(time)
    except IndexError:
        # If the threshold is never reached, append NaN (Not a Number)
        times_to_threshold.append(np.nan)

# --- Parametric loop to use only certain timesteps ---
for freq in frequencies:
    sol_freq = solve_ivp(system, [0, 0.3], y0, args=(U, R, C, L, freq), method='RK45', dense_output=True)  # Fixed: use freq not f
    
    last_01s_mask = sol_freq.t >= 0.2
    current_last_01s = sol_freq.y[0][last_01s_mask]
	
```
## Find Derivatives of State variables 
```python
derivatives = system(sol.t, sol.sol(sol.t), *sys_args)
curing_rate = derivatives[0]

## Using diff function 
# find first order differnce
np.diff(array, n=1)
# example
dH = np.diff(sol_c.y[0], 1)  # h
# plotting hint - da/dt has n-1 length, therefore you need to slice the original t
plot(sol.t[1:], da/dt, '-', label='Label1')
```
## Trouble Shooting 

1.  Clamping Variables to prevent numerical errors
	```python
	a = np.clip(a, 0, 1)
	```
