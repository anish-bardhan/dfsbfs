memo = {}

def fib(n):
    if n in memo:
        return memo[n]
    elif n<=1:
        return n
    else:
        f = fib(n - 1) + fib(n-2) + fib(n-3)
    memo[n] = f
    return f

print(fib(100))
