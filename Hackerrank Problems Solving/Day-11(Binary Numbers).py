# Hackerrank Problem 30 Days of Code - (Day 11)

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())  # Read the input number
    
    # Convert the number to its binary representation, removing the '0b' prefix
    binary_rep = bin(n)[2:]
    
    # Split the binary string by '0' to get groups of consecutive '1's
    groups_of_ones = binary_rep.split('0')
    
    # Find the length of the longest group of consecutive '1's
    max_consecutive_ones = max(len(group) for group in groups_of_ones)
    
    # Print the result
    print(max_consecutive_ones)
'''
Input (stdin)
5
Expected Output

'''