import re

# Read the number of test cases
num_cases = int(input().strip())

for _ in range(num_cases):
    pattern = input().strip()
    try:
        re.compile(pattern)  # Try to compile the regex
        print(True)
    except re.error:
        print(False)  # If an error occurs, it's an invalid regex

'''
Input (stdin)
2
.*\+
.*+

Expected Output
True
False

Explanation

.*\+ : Valid regex.
.*+: Has the error multiple repeat. Hence, it is invalid.
'''