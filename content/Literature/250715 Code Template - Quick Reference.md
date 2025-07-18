## 5️⃣ Quick Reference

### File Operations

```python
# Save/Load text
np.savetxt('data.txt', data, header='x y')
data = np.loadtxt('data.txt')

# Save multiple arrays
with open('results.txt', 'w') as f:
    f.write(f"Frequency: {freq}\n")
    np.savetxt(f, results)
```

### Error Handling

```python
try:
    result = risky_operation()
except ValueError as e:
    print(f"Error: {e}")
    result = default_value
```

### String Formatting

```python
# F-strings (preferred)
print(f"The error is {error:.2f}%")
print(f"Parameters: a={a:.3f}, b={b:.3f}")

# Format method
print("The {} has an error of {:.2f}%".format(name, error))
```

**💡 Pro Tips:**

1. Always check array dimensions before operations
2. Initialize all class attributes in `__init__`
3. Use meaningful variable names in exams
4. Comment complex calculations
5. Test edge cases (zero, negative values)