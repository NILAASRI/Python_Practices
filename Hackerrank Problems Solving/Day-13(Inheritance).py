# Hackerrank Problem 30 Days of Code - (Day 13)

class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
    #   Class Constructor
    #   
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    # Write your constructor here
    def __init__(self,firstName, lastName, idNumber, scores):
        Person.__init__(self,firstName, lastName, idNumber)
        self.scores = scores

    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function here
    def calculate(self):
        average = sum(self.scores) / len(self.scores)
        letter = " "
        
        if average < 40:
            letter = 'T'
        elif 40 <= average < 55:
            letter = 'D'
        elif 55 <= average < 70:
            letter = 'P'
        elif 70 <= average < 80:
            letter = 'A'
        elif 80 <= average < 90:
            letter = 'E'
        elif 90 <= average <= 100:
            letter = 'O'
        return(letter)
line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())
'''
Input (stdin)
Heraldo Memelli 8135627
2
100 80
Expected Output
Name: Memelli, Heraldo
ID: 8135627
Grade: O
'''