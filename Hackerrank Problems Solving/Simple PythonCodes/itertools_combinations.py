from itertools import combinations

# Read input
s, k = input().split()
k = int(k)

# Sort the string to ensure lexicographic order
s = sorted(s)

# Generate and print combinations from length 1 to k
for i in range(1, k + 1):
    for combo in combinations(s, i):
        print("".join(combo))
'''
Input (stdin)
HACK 2
Your Output (stdout)
A
C
H
K
AC
AH
AK
CH
CK
HK
'''