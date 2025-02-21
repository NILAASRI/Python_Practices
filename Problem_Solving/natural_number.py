#sum of n Natural Numbers
n=int(input("Enter the number:"))
num=int(input("Enter any numbers:"))
total=0
if(n>=1):
    for value in range(n,num+1):
        total=total+value
        print(value,end=" ")
    print("\nTotal value is:",total)   # Input=10, Output=55
else:
    print("....Less than 1 is not a natural number....")


