#This explain the string formatting method:
def print_formatted(number):
    # your code goes here
    width = len(bin(number)[2:])
    for i in range(1, number+1):
        print(f"{str(i).rjust(width)} {oct(i)[2:].rjust(width)} {hex(i)[2:].upper().rjust(width)} {bin(i)[2:].rjust(width)}")

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
    
'''
Input (stdin)
2
Expected Output
 1  1  1  1
 2  2  2 10

Let's Breakdown:
Decimal	Octal	Hex	Binary
1	1	1	1
2	2	2	10
Each column is right-aligned using width = 2 (since binary 10 has 2 digits).


'''
