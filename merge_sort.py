def mergesort(arr):
    if len(arr)<=1:
        return arr
    m=len(arr)//2
    left=arr[:m]
    right=arr[m:]
    left=mergesort(left)
    right=mergesort(right)
    return merge(left,right)
def merge(left,right):
    sorted_arr = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_arr.append(left[i])
            i += 1
        else:
            sorted_arr.append(right[j])
            j += 1
    sorted_arr += left[i:]
    sorted_arr += right[j:]
    return sorted_arr
array=[]
l=int(input("enter the length of array:"))
for i in range(l):
    e=int(input("enter the element:"))
    array.append(e)
print(mergesort(array))