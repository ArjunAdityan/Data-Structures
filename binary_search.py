
def binary_search(a,p,l,k,iter):
    if l>=p:
        mid=(p+l)//2
        if a[mid]==k:
            iter+=1
            return "iteration:",iter,"index:",mid
        elif k<a[mid]:
            iter+=1
            return binary_search(a,p,mid-1,k,iter)
        else:
            iter+=1
            return binary_search(a,mid+1,l,k,iter)
    else:
        return -1

n=int(input("enter length of array:"))
arr=[]
for i in range(n):
    ele=int(input())
    arr.append(ele)
k=int(input("enter element to search:"))
print(binary_search(arr,0,len(arr)-1,k,0))
