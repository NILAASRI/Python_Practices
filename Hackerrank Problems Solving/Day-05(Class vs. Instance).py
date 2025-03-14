# Hackerrank Problem 30 Days of Code - (Day 05)
class Person:
    def __init__(self,initialAge):
        # Add some more code to run some checks on initialAge
        if initialAge<0:
            print("Age is not valid, setting age to 0.")
            self.age = 0
        else:
            self.age = initialAge
    def amIOld(self):
        if self.age<13:
            print("You are young.")
        elif self.age>=13 and self.age<18:
            print("You are a teenager.")
        else:
            print("You are old.")
        # Do some computations in here and print out the correct statement to the console
    def yearPasses(self):
        # Increment the age of the person in here
        self.age += 1
    
t = int(input())
for i in range(0, t):
    age = int(input("Enter your age:"))         
    p = Person(age)  
    p.amIOld()
    for j in range(0, 3):
        p.yearPasses()       
    p.amIOld()
    print("")
    
    '''
Enter the value:4
Enter your age:-1
Age is not valid, setting age to 0.
You are young.
You are young.

Enter your age:10
You are young.
You are a teenager.

Enter your age:16
You are a teenager.
You are old.

Enter your age:18
You are old.
You are old.

    '''
