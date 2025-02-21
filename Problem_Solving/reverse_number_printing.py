# (1)
n=int(input("Enter the value: "))       
for i in range(n):                      
    for j in range(n-i-1):          
        print(" ",end="")
    for j in range(i+1): 
        print(j+1,end='')
    print(' ')
    
'''Enter the value: 5
    1 
   12 
  123 
 1234 
12345 '''



# (2)    
n=int(input("Enter the value: "))
for i in range(n):
    for j in range(n-i-1):
        print(" ",end="")
    for j in range(i,-1,-1): 
        print(j+1,end='')
    print(' ')

'''Enter the value: 5
    1 
   21 
  321 
 4321 
54321 '''



# (3)
n=int(input("Enter the value: "))
for i in range(n):
    for j in range(n-i-1):
        print(" ",end="")
    for j in range(i+1): # Also for j in range(i,-1,-1):
        print(i+1,end='')
    print(' ')

'''Enter the value: 5
    1 
   22 
  333 
 4444 
55555 '''



# (4)
n=int(input("Enter the value: "))
for i in range(n):
    for j in range(n-i-1):
        print(" ",end="")
    for j in range(i+1): 
        print(n-i,end='')
    print(' ')
    
'''Enter the value: 5
    5 
   44 
  333 
 2222 
11111 '''



# (5)
n=int(input("Enter the value: "))
for i in range(n):
    for j in range(n-i-1):
        print(" ",end="")
    for j in range(i+1): 
        print(n-j,end='')
    print(' ')
    
'''Enter the value: 5
    5 
   54 
  543 
 5432
54321 '''



# (6)
n=int(input("Enter the value: "))
for i in range(n):
    for j in range(n-i-1):
        print(" ",end="")
    for j in range(i,-1,-1): 
        print(n-j,end='')
    print(' ')

'''Enter the value: 5
    5 
   45 
  345 
 2345 
12345 '''



# (7) Half inverted pyramid
n=int(input("Enter the value:"))   
for i in range(n,0,-1):
    for j in range(n-i-1):
        print(" ",end="")
    for j in range(1,i+1):
        print(j,end=' ') 
    print()

'''
Enter the value:5
1 2 3 4 5 
1 2 3 4 
 1 2 3 
  1 2 
   1 
'''
# (8) Inverted pyramid
n=int(input("Enter the value:"))
a=0
for i in range(n,0,-1):
    for j in range(n-i-1):
        print(" ",end="")
    a+=1
    for j in range(1,i+1):
        print(a,end=' ')
    print()

'''Enter the value:5
1 1 1 1 1 
2 2 2 2 
 3 3 3 
  4 4 
   5
'''

# (9) 
n=int(input("Enter the value:"))
for i in range(n,0,-1):
    for j in range(n-i+1):
        print(" ",end="")
    num=i
    for j in range(0,i):
        print(num,end=' ')
    print()
'''
Enter the value:5
 5 5 5 5 5 
  4 4 4 4 
   3 3 3 
    2 2 
     1
     '''

# (10)
n=int(input("Enter the value:"))
for i in range(n+1):
    for j in range(n-i):
        print("",end=" ")
    num=n-i
    for j in range(0,i):
        print(num+1,end=' ')
    print()
'''
Enter the value: 5
     
    5 
   4 4 
  3 3 3 
 2 2 2 2 
1 1 1 1 1 
'''
    
