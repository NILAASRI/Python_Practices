# Hackerrank Problem 30 Days of Code - (Day 07)

# Get the number of test cases
t = int(input("Enter the number:"))

# Loop through each test case
for _ in range(t):
    # Get the string for the current test case
    s = input("Enter the value:")
    
    # Separate even and odd indexed characters
    even_chars = s[::2]  # Characters at even indices (0, 2, 4, ...)
    odd_chars = s[1::2]   # Characters at odd indices (1, 3, 5, ...)
    
    # Print even and odd indexed characters space-separated
    print(even_chars, odd_chars)

'''
Sample Input
2
Hacker
Rank

Sample Output
Hce akr
Rn ak

'''