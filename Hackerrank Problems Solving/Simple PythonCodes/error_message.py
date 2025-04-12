# Read number of test cases
t = int(input())

for _ in range(t):
    try:
        # Read inputs and split into two numbers
        a, b = input().split()
        
        # Convert to integers
        a, b = int(a), int(b)
        
        # Perform integer division
        print(a // b)
    
    except ZeroDivisionError:
        print("Error Code: integer division or modulo by zero")
    
    except ValueError as e:
        print(f"Error Code: {e}")

'''
Input (stdin)
3
1 0
2 $
3 1
Expected Output
Error Code: integer division or modulo by zero
Error Code: invalid literal for int() with base 10: '$'
3
'''