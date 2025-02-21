# Find the largest number 
# (1)
print("----------Type 1- To find first largest number----------")
def largest(arr,n):
    ans=max(arr)
    return ans
if __name__ == '__main__':
    arr=[10,32,45,90,9808]
    n=len(arr)
    print("The largest numbers is ",largest(arr,n))
print("                                             ")  #This print function is just for space 
    
# (2)    
print("----------Type 2 - To find first largest number----------")
def largest_num1(arrays,n):
    max_value=arrays[0]
    for i in range(1,n):
        if arrays[i]>max_value:
            max_value=arrays[i]
    return max_value     
arrays=[10,2,30,45,55,121]
n=len(arrays)
answer=largest_num1(arrays, n)
print("Largest number:",answer)
print("                                             ")  #This print function is just for space 
    
   
# Find the second largest number
print("----------Second largest number----------")
def second_largest(numbers):
    largest_num=max(numbers)
    numbers.remove(largest_num)
    return max(numbers)
numbers=[10,20,3,4,45,99,121]
print("The second largest number is :", second_largest(numbers))