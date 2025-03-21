# Hackerrank Problem 30 Days of Code - (Day 17)
'''
Task
Write a Calculator class with a single method: int power(int,int). The power method takes two integers,  and , as parameters and returns the integer result of . If either  or  is negative, then the method must throw an exception with the message: n and p should be non-negative.

Note: Do not use an access modifier (e.g.: public) in the declaration for your Calculator class.
'''

#Write your code here
class Calculator:

    def power(self, n, p):
        if n < 0 or p < 0:
          raise Exception("n and p should be non-negative")
        else:
            return n**p

myCalculator=Calculator()
T=int(input())
for i in range(T):
    n,p = map(int, input().split())
    try:
        ans=myCalculator.power(n,p)
        print(ans)
    except Exception as e:
        print(e)   
        
'''
Input (stdin)
4
3 5
2 4
-1 -2
-1 3
Your Output (stdout)
243
16
n and p should be non-negative
'''