n = int(input("Enter the number of values to be get:"))
stamp = set()
for i in range(n):
    stamp.add(input("Enter the country:"))
print(len(stamp))

'''
Input:
7
UK
China
USA
France
New Zealand
UK
France

Output:
5
'''