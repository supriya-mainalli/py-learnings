arr = [2, 5, 1, 7, 10]

def longest_substring(arr,k):
    i,j = 0,0
    max_len = 0
    start = 0
    end = 0
    for i in range(len(arr)):
        sum = 0
        for j in range(i, len(arr)):
            sum = sum + arr[j]
            if(sum<=k):
                max_len = max(max_len, j-i+1)
            else:
                break
    return max_len, [start, end]

print(longest_substring(arr, 14))

