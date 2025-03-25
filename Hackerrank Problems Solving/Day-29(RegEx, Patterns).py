# Hackerrank Problem 30 Days of Code - (Day 29)
#RegEx, Patterns, and Intro to Databases

#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input().strip())
    gmail = [ ]

    for N_itr in range(N):
        first_multiple_input = input().rstrip().split()

        firstName = first_multiple_input[0]

        emailID = first_multiple_input[1]
        domain = emailID.split("@")[1]
        
        if domain == "gmail.com":
            gmail.append(firstName)
        
    gmail.sort()
    for fn in gmail:
        print(fn)

'''
Input (stdin)
6
riya riya@gmail.com
julia julia@julia.me
julia sjulia@gmail.com
julia julia@gmail.com
samantha samantha@gmail.com
tanya tanya@gmail.com

Expected Output
julia
julia
riya
samantha
tanya
'''