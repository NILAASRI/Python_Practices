# To check the prime number
num= 121
if num>1:
    for i in range(2,(num//2)+1):
        if num%i==0:
            print(num," is not a prime")
            break
        else:
            print(num," is prime")
            break
else:
    print(num,"is not a prime")
    
    
#Print the prime numbers
prime=[]
n=int(input("Enter the number:"))
for possibleprime in range(2,n):
    isprime=True
    for num in range(2,possibleprime):
        if possibleprime%num==0:
            isprime=False
    if isprime:
        prime.append(possibleprime)
print(prime)
