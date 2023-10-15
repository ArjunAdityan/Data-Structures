def LIS(arr):
    L = [0] * len(arr)
    L[0] = 1
    for i in range(1, len(arr)):
        for j in range(i):
            if arr[j] < arr[i] and L[j] > L[i]:
                L[i] = L[j]

        L[i] = L[i] + 1
    return max(L)

    '''def lis(nums):
    n = len(nums)
    lis = [1] * n  # Table to store lengths of increasing subsequences

    for i in range(1, n):
        for j in range(i):
            if nums[i] > nums[j] and lis[i] < lis[j] + 1:
                lis[i] = lis[j] + 1

    max_length = max(lis)  # Length of the longest increasing subsequence

    # Reconstruct the longest increasing subsequence
    subsequence = []
    max_index = lis.index(max_length)
    subsequence.append(nums[max_index])
    for i in range(max_index - 1, -1, -1):
        if nums[i] < nums[max_index] and lis[i] == lis[max_index] - 1:
            subsequence.insert(0, nums[i])
            max_index = i

    return max_length, subsequence


array=[5,1,10,4,11]
print(lis(array))'''
