def linearsearch(A,x):
    l=len(A)
    i=0
    while i<l:
        if A[i]==x:
            print(i)
            return True
        i+=1
    return False
length=int(input("enter length of list:"))
list=[]
for i in range(length):
    m=int(input("enter the number:"))
    list.append(m)
element=int(input("enter the value x"))
a=linearsearch(list,element)
print(a)