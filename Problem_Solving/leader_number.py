#Leader Number - The number should be greater than all the numbers present in the right side
a=[17,1,5,3,2,4,16,7,8,14] #last number is always a leader number
b=[]
for i in range(0,len(a)):
    isleader=True #Boolean action 
    for j in range(i+1,len(a)):
        if(a[i]<a[j]):
            isleader=False
            break
    if(isleader):
        b.append(a[i])
print(b)
