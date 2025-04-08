# Read the number of students
num_students = int(input().strip())

# Read column headers and split into a list
columns = input().strip().split()

# Find index of "MARKS" column
marks_index = columns.index("MARKS")

# Read student data and extract marks
total_marks = 0
for _ in range(num_students):
    student_data = input().strip().split()
    total_marks += int(student_data[marks_index])

# Calculate average marks
average_marks = total_marks / num_students

# Print the result rounded to 2 decimal places
print(f"{average_marks:.2f}")

'''
Input (stdin)
5
ID         MARKS      NAME       CLASS
1          97         Raymond    7
2          50         Steven     4
3          91         Adrian     9
4          72         Stewart    5
5          80         Peter      6

Expected Output
78.00

Explanation
Average = (97+50+91+72+80)/5
'''
