#Define a reverse function
def rev_func(string):
    revstr = ''
    for x in string:
        revstr = x + revstr
    return revstr
 
string = str(input("Enter the string:"))
#print('Original String: ', string)
print('Reverse String: ', rev_func(string))


#Another type for string
print("----------------Reverse string type-2-----------------")
a=input("Enter the string:")
b=a[::-1]
print(b)



#Reverse for numbers
print("---------------Numbers reverse using for loop------------------")
for i in range(10,0,-1):
    print(i,end=" ")
