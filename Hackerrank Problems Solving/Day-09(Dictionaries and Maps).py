# Hackerrank Problem 30 Days of Code - (Day 09)

# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
k={}
for i in range(n):
    name,ph=input().split()
    k[name]=int(ph)
try:
    while True:
        inp=input()
        if inp in k:
            print(f'{inp}={k[inp]}')
        else:
            print('Not found')
except EOFError:
    pass

'''
Input (stdin)
3
sam 99912222
tom 11122222
harry 12299933
sam
edward
harry
Expected Output
sam=99912222
Not found
harry=12299933
'''