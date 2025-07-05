---
title: Claude's Exam Prep Strategy
draft: true
tags: 
date: 2025-05-22
---
## Core Topic Distribution

### 1. **Data Processing & Plotting (15-20 points) - ALWAYS PRESENT**

- Reading CSV/data files (numpy, pandas)
- Matplotlib plotting with specific formatting
- Curve fitting (scipy.curve_fit, numpy.polyfit)
- Data analysis and visualization

**Quick tip for cheatsheet:** This appears in EVERY exam! Include templates for reading files, basic plot formatting, and curve fitting code.

### 2. **Differential Equations (20 points) - ALWAYS PRESENT**

- ODE solving using scipy.solve_ivp or scipy.odeint
- Spring-mass-damper systems
- Predator-prey models
- Chemical/thermal reaction models
- Electrical circuits

**Quick tip for cheatsheet:** Have scipy.solve_ivp syntax ready with different solver options (RK45, Radau, etc.)

### 3. **Object-Oriented Programming (15-20 points) - FREQUENT**

- Class definition with `__init__`
- Properties and setters
- Protected attributes (underscore convention)
- Magic methods
- UML diagram implementation

### 4. **Numerical Methods (10-15 points) - OCCASIONAL**

- Root finding (scipy.optimize.newton)
- Interpolation (numpy.interp)
- Integration
- Equation solving

### 5. **Debugging/Error Correction (5-10 points) - OCCASIONAL**

- Fix provided buggy code
- Function parameter corrections

## Specific Recurring Patterns

1. **File I/O patterns:**
    
    - CSV files with experimental data
    - Two-column format (x,y data)
    - Sometimes multiple files to compare
2. **Plotting requirements:**
    
    - Multiple curves on same plot
    - Specific line styles (solid, dashed, dash-dot)
    - Legends with formatted strings
    - Grid enabled
    - Axis labels and limits
    - Text annotations for specific points
    - Subplots (often 2x1 layout)
3. **ODE patterns:**
    
    - Coupled systems (2+ equations)
    - Physical systems with given parameters
    - Time evolution plots
    - Parameter variation studies

## Preparation Strategy

1. **Practice past exams** - The patterns are very consistent
2. **Master the basics** - File I/O, plotting, and scipy.solve_ivp are guaranteed
3. **Focus on formatting** - Exams are very specific about plot appearance
4. **Understand physical systems** - Spring-damper, electrical circuits, chemical reactions
5. **Keep reference snippets handy** - You'll need exact syntax for scipy functions

The exam format is quite predictable, with plotting and ODEs being the bread and butter of every exam. Success comes from being efficient with these core tasks to leave time for the more challenging variations.
