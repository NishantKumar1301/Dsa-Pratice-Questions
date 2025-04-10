#Question : Absolute Sorting
#Link to the question: https://codeforces.com/contest/1772/problem/D

# cook your dish here
def binarysearch(low, high, arr, n):
    while low <= high:
        mid = (low + high) // 2
        flag = 0
        for i in range(n - 1):
            if abs(arr[i] - mid) > abs(arr[i + 1] - mid):
                if arr[i] > arr[i + 1]:
                    flag = 1
                else:
                    flag = 2
                break
        if flag == 1:
            low = mid + 1
        elif flag == 2:
            high = mid - 1
        else:
            return mid
    return -1

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    ans = binarysearch(0, 10**9, arr, n)
    print(ans)

