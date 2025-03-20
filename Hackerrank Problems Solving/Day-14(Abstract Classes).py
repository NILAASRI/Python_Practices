# Hackerrank Problem 30 Days of Code - (Day 14)

from abc import ABCMeta, abstractmethod
class Book(object, metaclass=ABCMeta):
    def __init__(self,title,author):
        self.title=title
        self.author=author   
    @abstractmethod
    def display(): pass

#Write MyBook class
class MyBook(Book):
    def __init__(self,title, author, price):
        self.title = title
        self.author = author
        self.price = price
    def display(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Price: {self.price}")
title=input()
author=input()
price=int(input())
new_novel=MyBook(title,author,price)
new_novel.display()

'''
Input (stdin)
The Alchemist
Paulo Coelho
248
Expected Output
Title: The Alchemist
Author: Paulo Coelho
Price: 248
'''