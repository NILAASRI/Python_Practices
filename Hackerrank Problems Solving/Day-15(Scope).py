# Hackerrank Problem 30 Days of Code - (Day 15)

class Difference:
    def __init__(self, a):
        self.__elements = a
        self.maximumDifference = 0  # Initialize the maximum difference

    def computeDifference(self):
        # Compute the maximum absolute difference
        self.maximumDifference = max(self.__elements) - min(self.__elements)
# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)

'''
Input (stdin)
3
1 2 5
Expected Output
4
'''