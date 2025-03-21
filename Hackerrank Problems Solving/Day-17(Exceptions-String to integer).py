# Hackerrank Problem 30 Days of Code - (Day 17)
'''
Task
Read a string, , and print its integer value; if  cannot be converted to an integer, print Bad String.

Note: You must use the String-to-Integer and exception handling constructs built into your submission language. If you attempt to use loops/conditional statements, you will get a  score.

Input Format

A single string, .
'''
#!/bin/python3

import math
import os
import random
import re
import sys

S = input("Enter the string:").strip()
try:
    S = int(S)
    print(S)
except:
    print("Bad String")

'''
Sample Input 1
3

Sample Output 1
3

Sample Input 2
za

Sample Output 2
Bad String
'''