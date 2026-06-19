# given the array, find the max sum obtained by picking k elements consecutively


arr = [-1, 2, 3, 4, 5, -1]

def max_subarray(arr, k):
    l = 0
    r = k-1
    n = len(arr)
    sum = 0

    for i in range(k):
        sum = sum + arr[i]

    max_sum = sum

    while(r<n-1):
        sum = sum - arr[l]
        l += 1
        r += 1
        sum = sum + arr[r]
        max_sum = max(max_sum, sum)
    return max_sum

print(max_subarray(arr, 4))