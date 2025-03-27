def average(array):
    # your code goes here
    length = len(set(array))
    avg = sum(set(array)) / (length)
    return round(avg,3)

if __name__ == '__main__':
    n = int(input("Enter the value:"))
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
    
'''
Input (stdin)
10
161 182 161 154 176 170 167 171 170 174
Your Output (stdout)
169.375
'''
