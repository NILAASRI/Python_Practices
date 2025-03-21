# Hackerrank Problem 30 Days of Code - (Day 21)
'''Given an array,a, of size n distinct elements, sort the array in ascending order 
using the Bubble Sort algorithm above.'''
#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input("Enter the number:").strip())

    a = list(map(int, input("Enter the values:").rstrip().split()))

    # Write your code here
    swap=0
    for i in range(n):
        for j in range(n-i-1):
            if a[j]>a[j+1]:
                swap+=1
                a[j],a[j+1]=a[j+1],a[j]
    print(f'Array is sorted in {swap} swaps.')
    print(f'First Element: {a[0]}')
    print(f'Last Element: {a[-1]}')
    
'''
Input (stdin)
3
1 2 3
Your Output (stdout)
Array is sorted in 0 swaps.
First Element: 1
Last Element: 3
'''