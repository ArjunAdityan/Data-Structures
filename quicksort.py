def partition(a,p,l):
    r=a[l]
    i = p-1
    for j in range(p,l):
        if a[j]<=r:
            i = i + 1
            a[i],a[j]=a[j],a[i]
    a[i+1],a[l]=a[l],a[i + 1]
    return i + 1


def quick_sort(a,p,l):
    if p < l:
        q=partition(a,p,l)
        quick_sort(a,p,q-1)
        quick_sort(a,q+1,l)

arr=[]
n=int(input("enter length of array:"))
for i in range(n):
    ele=int(input())
    arr.append(ele)
quick_sort(arr, 0, len(arr) - 1)
print(arr)
