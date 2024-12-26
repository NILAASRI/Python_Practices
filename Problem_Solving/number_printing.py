# (1) Number increasing pyramid type-1
n=int(input("Enter the value: "))
for i in range(0,n+1):
    for j in range(1,i+1):
        print (i,end='')
    print("")
    
# (2) Number increasing pyramid type-2
n=int(input("Enter the value: "))
for i in range(n+1):
    for i in range(1,i+1):
        print(i,end='')
    print(' ')
    
# (3) Number changing pyramid
n=int(input("Enter the value: "))
num=1
for i in range(0,n):
    for j in range(0,i+1):
        print(num,end=' ')
        num+=1
    print()
