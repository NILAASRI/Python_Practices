a=[1,2,3,4,5,6,7,8,9] # 3 types of list assign  =  direct, .copy(), list(a)
#b1=list(a)
#c1=a.copy()
#print(a,b1,c1)
#variable name[start index,end index,step]
b=a[0:3:1]
c=a[1:7:2]
d=a[1:-4]   #negative index
print(b)
print(c)
print(d)
a1=[1,2,3,4,5,5,6,7,8,8,'hi']  #here list allows a duplicate
print(a1)


#append operation
print("..........Append operation.........")
e=[1,2,3]
e.append(5)
print(id(e)) #same memory location
print(e)
print(e.append(8)) #it cannot return any funtion so it output is none
print(e) #but this print line executes the append(8) operation here

print("Append operation shadow copy ")
e3=e
print(e3)
print(id(e),id(e3)) #same memory location even after append any number

e4=[11,12,13]
e5=e4.copy()
e4.append(14)
print(e4)
print(e5)


print(".........Insert.........")
#insert function
f=[5,7,8]
f.insert(1,6)#4 can be stored in index 1
f.insert(0,4) 
print(f)

print(".........remove..........")
#remove element
g=[6,7,8]
g1=[6,7,7,7,8]
g.remove(8)
g1.remove(7)
print(g)
print(g1)

#count
h=[1,2,2,2,3,4]
h.count(2)
print(h.count(2))

#delete function
i=[1,2,3,4,5,6,7]
del i
print()

print("..........reverse and length.............")
i1=[1,2,3,4,5,6,7]
print(len(i1))  #length function
i1.reverse()  #reverse function   ,this reverse function replace the original array into reverse array 
print(i1)
print(i1.reverse()) #this print the none

#alternate of reverse function    ,but this type of reverse funciton cannot replace the value because we access this function by its index,
i2 = ['a','b','c','d','e']
print(i2[::-1])
print(i2)


#def function
print(".........del function()........")
def hello():
    return('Nice to meet you')
print(hello())

def hi():
    a=[4,3,2] #if we didn't return any type it shows output with none
print(hi())

#memory location address
print("............memory location..........")
j=30
j1=30

k=[1,2]
k1=[1,2] #different memory location
k2=k #same memory location of k
print(id(j),id(j1))
print(id(k),id(k1))
print(id(k),id(k2))

#In tuple we cannot modify after once create 
print("..........Tuple............")
l = (21,22,23,24,25)
print(l[0])
l1 = list(l) # we change it into list
print(l1)

#set
print("...........Set{}.............")
m = {1,2,3}
print(type(m))

    #set add
m.add(4)
m.add(1) # set cannot store the duplicate element
print(m)

    #set pop
print("Pop function")
m1 = {6,7,8,4,2,1,11,5}
print(m1)
#m1.pop()
#print(m1)

m2= {10,2,5,9,8,7}
print(m2)
#m2.pop()
#print(m2)

m3={4,3,2,1} #Also check m3 ={9,8,7,6} and m3 = {9,8,7,6,5}
print(m3)


#Task_1
numbers_input = input("Enter numbers:")
numbers = numbers_input.split()
unique_numbers = set(numbers)
for number in unique_numbers:
    print(number,"is present",numbers.count(number),"times")