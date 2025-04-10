from collections import deque

# Read number of operations
n = int(input())

# Initialize an empty deque
d = deque()

# Perform operations
for _ in range(n):
    operation = input().split()
    if operation[0] == "append":
        d.append(int(operation[1]))
    elif operation[0] == "appendleft":
        d.appendleft(int(operation[1]))
    elif operation[0] == "pop":
        d.pop()
    elif operation[0] == "popleft":
        d.popleft()

# Print elements in deque
print(*d)

'''
Input (stdin)
6
append 1
append 2
append 3
appendleft 4
pop
popleft

Expected Output
1 2
'''