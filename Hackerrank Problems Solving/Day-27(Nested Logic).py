# Hackerrank Problem 30 Days of Code - (Day 27)

def calculate_fine(d1, m1, y1, d2, m2, y2):
    if (y1, m1, d1) <= (y2, m2, d2):
        return 0  # No fine if returned on or before the due date
    
    if y1 > y2:
        return 10000  # Fixed fine if returned after the expected year
    
    if m1 > m2 and y1 == y2:
        return 500 * (m1 - m2)  # Fine per month late within the same year
    
    if d1 > d2 and m1 == m2 and y1 == y2:
        return 15 * (d1 - d2)  # Fine per day late within the same month
    
    return 0  # Default case, no fine

# Input
actual_day, actual_month, actual_year = map(int, input().split())
due_day, due_month, due_year = map(int, input().split())

# Compute and print the fine
print(calculate_fine(actual_day, actual_month, actual_year, due_day, due_month, due_year))

'''
Input (stdin)
9 6 2015
6 6 2015
Expected Output
45
'''