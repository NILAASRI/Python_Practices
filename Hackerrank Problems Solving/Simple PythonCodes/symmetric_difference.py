# Read input values
m = int(input())
a = set(map(int, input().split())) #converts space-separated input numbers into a set of integers.
n = int(input())
b = set(map(int, input().split()))

# Compute symmetric difference
sym_diff = a.symmetric_difference(b)#a.symmetric_difference(b) or a ^ b: gives the elements in either a or b but not in both.

# Print the result in ascending order
for num in sorted(sym_diff):
    print(num)

'''
Sample Input

STDIN       Function (This function explains how the input checks the size of both set)
-----       --------
4           set a size M = 4
2 4 5 9     a = {2, 4, 5, 9}
4           set b size N = 4
2 4 11 12   b = {2, 4, 11, 12}

Sample Output

5
9
11
12
'''
