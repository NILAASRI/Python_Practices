# Hackerrank Problem 30 Days of Code - (Day 23)
def print_array(value):
    for item in value:
        print(item)

def main():
    # Reading the number of elements for the first list
    n = int(input())
    int_array = []
    for _ in range(n):
        int_array.append(int(input()))
    
    # Reading the number of elements for the second list
    n = int(input())
    string_array = []
    for _ in range(n):
        string_array.append(input())
    
    # Print the arrays
    print_array(int_array)
    print_array(string_array)

# Call main function
if __name__ == "__main__":
    main()
    
'''
Input (stdin)
3
1
2
3
2
Hello
World


Your Output (stdout)
1
2
3
Hello
World
'''