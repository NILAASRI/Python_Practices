# Hackerrank Problem 30 Days of Code - (Day 16)
'''
Task :
Complete the insert function in your editor so that it creates a new Node (pass  as the Node constructor 
argument) and inserts it at the tail of the linked list referenced by the  parameter. Once the new node is 
added, return the reference to the  node.
Note: The  argument is null for an empty list.
'''
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
class Solution: 
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    def insert(self,head,data): 
        new_node = Node(data)
        if head is None:
            self.prev = new_node
            return new_node
        else:
            self.prev.next = new_node
            self.prev = new_node
        return head
       
mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)    
mylist.display(head); 