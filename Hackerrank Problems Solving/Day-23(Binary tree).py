# Hackerrank Problem 30 Days of Code - (Day 22)

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Solution:
    def insert(self, root, data):
        if root is None:
            return Node(data)
        else:
            if data < root.data:
                root.left = self.insert(root.left, data)
            else:
                root.right = self.insert(root.right, data)
        return root
    
    def getHeight(self, root):
        # If the tree is empty, the height is -1
        if root is None:
            return -1
        
        # Recursively calculate the height of the left and right subtrees
        left_height = self.getHeight(root.left)
        right_height = self.getHeight(root.right)
        
        # The height of the current node is the maximum of the heights of its subtrees plus 1
        return max(left_height, right_height) + 1

# Main function to drive the program
T = int(input())  # Number of nodes to insert
myTree = Solution()
root = None

# Inserting nodes into the binary search tree (BST)
for _ in range(T):
    data = int(input())
    root = myTree.insert(root, data)

# Getting the height of the binary tree
height = myTree.getHeight(root)
print(height)

'''
Input (stdin)
7
3
5
2
1
4
6
7
Your Output (stdout)
3

'''