   
## Definition
A recursion is a concept where a function calls on itself to solve a problem. Instead of using loops (while , for), the function calls on itself. 

## Stack Over Flow
It is the most common type of error when dealing with recursions. It happens when there is no base case that the Function approaches to and hence the function keeps running till the end of memory. 
### **Example:** Function to calculate the factorial
```python
def factorial(n):
    # Base case: if n is 1, just return 1 since 1! = 1
    if n == 1:
        return 1
    # Recursive case: n! = n * (n-1)!
    else:
        return n * factorial(n-1)
```





