# Hackerrank Problem 30 Days of Code - (Day 25)

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
class Solution: 
    def insert(self,head,data):
            p = Node(data)           
            if head==None:
                head=p
            elif head.next==None:
                head.next=p
            else:
                start=head
                while(start.next!=None):
                    start=start.next
                start.next=p
            return head  
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    def removeDuplicates(self,head):
        #Write your code here
        if head is None:
            return head
        
        seen = set()
        current = head
        seen.add(current.data)
        
        while current.next:
            if current.next.data in seen:
                current.next = current.next.next  # Skip duplicate node
            else:
                seen.add(current.next.data)
                current = current.next
        
        return head

mylist= Solution()
T=int(input("Enter the number: "))
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)    
head=mylist.removeDuplicates(head)
mylist.display(head); 

'''
Input (stdin)
6
1
2
2
3
3
4
Expected Output
1 2 3 4
'''