# Hackerrank Problem 30 Days of Code - (Day 04)
#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input("Enter the value:").strip())
def weird_test(N):
    if (N % 2 != 0) or(6 <= N <= 20):
        print("Weird")
    else:
        print("Not Weird")
weird_test(N)