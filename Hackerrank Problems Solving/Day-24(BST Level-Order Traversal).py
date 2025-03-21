# Hackerrank Problem 30 Days of Code - (Day 24)

import sys

class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def levelOrder(self,root):
        #Write your code here
        queue = [root]
        for item in queue:
            if item.left:
                queue.append(item.left)
            if item.right:
                queue.append(item.right)
        print(" ".join([str(i.data) for i in queue]))

T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
myTree.levelOrder(root)

'''
Input (stdin)
6
3
5
4
7
2
1
Expected Output
3 2 5 1 4 7
'''