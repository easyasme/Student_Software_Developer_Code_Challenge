# 1. Write a function that will reverse the given input string.
def reverse_string(input_string: str) -> str:
    return input_string[::-1]

# Test
print(reverse_string("abcdefg"))


# 2. Write a function that accepts three integers as input and returns as output the largest of the three.
def largest_of_three_ints(num1: int, num2: int, num3: int) -> int:
    return max(num1, num2, num3)

# Test
print(max(10, 20, 15))


# 3. Write a function that calculates the factorial of an input integer using recursion.
def factorial(n: int):
    if (n < 0): return "Error due to negative integer"
    elif (n == 0 or n == 1): return 1

    return n * factorial(n - 1)

# Test
print(factorial(-1))
print(factorial(0))
print(factorial(7))


# 4. Write a function that calculates the Nth entry of the Fibonacci sequence (Do not include 0 in the sequence).
def fibonacci(n: int):
    if (n <= 0): return "Error due to zero or negative integer"
    elif (n == 1 or n == 2): return 1

    fibonacci_sequence = [0 for i in range(n)]
    fibonacci_sequence[0] = fibonacci_sequence[1] = 1
    for i in range(2, n):
        fibonacci_sequence[i] = fibonacci_sequence[i - 1] + fibonacci_sequence[i - 2]

    return fibonacci_sequence[n - 1]

# Test
print(fibonacci(0))
print(fibonacci(1))
print(fibonacci(2))
print(fibonacci(10))