# 1) Right Half Pyramid 
n=int(input("Enter the value: "))
for i in range(n):
    print("*"*(i+1))
    
''' 
# This program using function call method. We also use without function for this same program(--refer no.(3)-- for without function method)
def diamond(n):
    n=int(input("Enter the value: "))
    for i in range(0,n):
        for j in range(0,i+1):
            print("*",end='')
        print()
diamond(n)
'''


# 2) Left Half Pyramid
n=int(input("Enter the value: "))
for i in range(n):
      #print spaces
    for j in range(n-i-1):
        print(" ",end="")
      #print stars
    for k in range(i+1):
        print("*",end="")
    print()
        
        
# 3) Reverse right half pyramid
n=int(input("Enter the value: "))
for i in range(n,0,-1):
    print("*"*i)
    
'''n=int(input("Enter the value:))
   for i in range(n,0,-1):
        for j in range(0,i):
            print("*",end="")
        print()
'''
    
    
# 4) Reverse left half pyramid
n=int(input("Enter the value: "))
for i in range(n,0,-1):
    #print spaces
    for j in range(n-i):
        print(" ",end="")
    #print stars
    for k in range(i):
        print("*", end="")
    print()
    
    
# 5) Hollow Pattern
n=int(input("Enter the value: "))
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1:
            print("*",end='')
        else:
            print(" ",end='')
    print()
    
    
# 6) Triangle star pattern
n=int(input("Enter the value: "))
k=n-1
for i in range(0,n):
    for j in range(0,k):
        print(end=" ")
    k=k-1
    for j in range(0,i+1):
        print("*",end=' ')
    print()