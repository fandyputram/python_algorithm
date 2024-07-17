def fibonacci(n):
    if n <= 1:
        return n
    else:
        fibonacci(n-1) + fibonacci(n-2)
        
print(fibonacci(10))

def fibonacci_iterative(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

# Example usage
n = 10
print(f"Fibonacci({n}) using iteration is {fibonacci_iterative(n)}")
