# Hackerrank Problem 30 Days of Code - (Day 10)

#!/bin/python3

import math
import os
import random
import re
import sys

def factorial(n):
    # Write your code here
    if (n==0 or n==1):
        return 1
    else:
        return n*factorial(n-1)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = factorial(n)

    fptr.write(str(result) + '\n')

    fptr.close()

'''
Sample Input
3
Sample Output
6
'''