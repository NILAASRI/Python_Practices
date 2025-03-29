#itertools permutations
from itertools import permutations

s, k = input("Enter the word and no. of pairs: ").split()
k = int(k)

for p in sorted(permutations(s, k)):
    print(''.join(p))

'''
Input
HACK 2
Expected Output
AC
AH
AK
CA
CH
CK
HA
HC
HK
KA
KC
KH

'''