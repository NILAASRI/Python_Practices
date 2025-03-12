# Hackerrank Problem 30 Days of Code - (Day 03)

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the 'solve' function below.
# The function accepts following parameters:
#  1. DOUBLE meal_cost
#  2. INTEGER tip_percent
#  3. INTEGER tax_percent

def solve(meal_cost, tip_percent, tax_percent):
    # Write your code here
    tip = (tip_percent/100) * meal_cost 
    tax = (tax_percent/100) * meal_cost

    total_price = round(tax + tip + meal_cost)
    print(total_price)

if __name__ == '__main__':
    meal_cost = float(input("Enter the value:").strip())

    tip_percent = int(input("Enter the value:").strip())

    tax_percent = int(input("Enter the value:").strip())

    solve(meal_cost, tip_percent, tax_percent)


'''
Example
A tip of 15% * 100 = 15, and the taxes are 8% * 100 = 8. 
Print the value  and return from the function.

Sample Input

12.00
20
8
Sample Output

15
'''