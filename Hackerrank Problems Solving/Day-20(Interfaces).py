# Hackerrank Problem 30 Days of Code - (Day 20)

class AdvancedArithmetic(object):
    def divisorSum(n):
        raise NotImplementedError

class Calculator(AdvancedArithmetic):
    def divisorSum(self, n):
        sum = 0
        for i in range(1, n+1):
            if n % i == 0:
                sum += i
        return sum

n = int(input("Enter the value:"))
my_calculator = Calculator()
s = my_calculator.divisorSum(n)
print("I implemented: " + type(my_calculator).__bases__[0].__name__)
print(s)

'''
OUTPUT 
Enter the value:6
I implemented: AdvancedArithmetic
12

'''