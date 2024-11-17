#Palindrome for string
a=input("Enter the value:")
b=a[::-1]
if a==b:
    print("It is a palindrome")
else:
    print("It is not a palindrome")
 
    
# function which return reverse of a string
def isPalindrome(s):
    return s==s[::-1]
s = input("Enter the string:")
ans = isPalindrome(s)
if ans:
    print("Yes,It is a palindrome")
else:
    print("No, It is not a palindrome")
    

#For numbers
def is_palindrome(num):
    num_str=str(num)
    return num_str==num_str[::-1] #Also here we use reverse_str=num_str[::-1]; return num_str=reverse_str
number=int(input("Enter a number: "))
if is_palindrome(number):
    print(f"{number} is a palindrome.")
else:
    print(f"{number} is not a palindrome.")