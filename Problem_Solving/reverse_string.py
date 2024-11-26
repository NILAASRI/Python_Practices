#Define a reverse function
def rev_func(string):
    revstr = ''
    for x in string:
        revstr = x + revstr
    return revstr
 
string = str(input("Enter the string:"))
#print('Original String: ', string)
print('Reverse String: ', rev_func(string))
