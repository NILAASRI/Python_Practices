# Hackerrank Problem 30 Days of Code - (Day 26)

import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# Read number of test cases
t = int(input())

# Check each number for primality
for _ in range(t):
    n = int(input())
    if is_prime(n):
        print("Prime")
    else:
        print("Not prime")

'''
Input (stdin)
3
12
5
7
Expected Output
Not prime
Prime
Prime
'''