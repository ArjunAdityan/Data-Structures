def insertion_sort(arr):
    n=len(arr)
    for i in range(1,n):
        key=arr[i]
        j=i-1
        while j>=0 and key < arr[j]:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
    return arr

n=int(input("enter length of array:"))
lst=[]
for i in range(n):
    ele=int(input())
    lst.append(ele)
print(insertion_sort(lst))
