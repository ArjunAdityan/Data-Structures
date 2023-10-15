def bubblesort(l):
    length=len(l)
    for i in range(length):
        for j in range(length-i-1):
            if l[j]>l[j+1]:
                l[j],l[j+1]=l[j+1],l[j]
    return l
num=int(input("enter no.of elements :"))
list=[]
for k in range(num):
    element=int(input())
    list.append(element)
print(bubblesort(list))
