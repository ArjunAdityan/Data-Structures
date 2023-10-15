def computeFibonacci(n):
    if n <= 1:
        return n

    fib_table = [0] * (n + 1)
    fib_table[1] = 1

    for i in range(2, n + 1):
        fib_table[i] = fib_table[i - 1] + fib_table[i - 2]

    return fib_table[n]

n = int(input("Enter the value of n: "))
result = computeFibonacci(n)
print("The Fibonacci number is:", result)