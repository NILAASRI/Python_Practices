n = int(input())
s = list(map(int, input().split()))
s = list(dict.fromkeys(s))  # remove duplicates, preserve order
num_commands = int(input())

for _ in range(num_commands):
    cmd = input().strip().split()
    if cmd[0] == 'pop':
        if s:
            s.pop(0)  # pop from the beginning (simulate correct behavior)
    elif cmd[0] == 'remove':
        val = int(cmd[1])
        if val in s:
            s.remove(val)
    elif cmd[0] == 'discard':
        val = int(cmd[1])
        if val in s:
            s.remove(val)

print(sum(s))

'''
Input:
9
1 2 3 4 5 6 7 8 9
10
pop
remove 9
discard 9
discard 8
remove 7
pop
discard 6
remove 5
pop
discard 5

Output:
4

'''