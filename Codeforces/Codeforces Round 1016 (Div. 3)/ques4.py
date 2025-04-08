#Question : Min Max MEX
#Link to the question: https://codeforces.com/contest/2093/problem/E


def solve(arr, n, k, mid):
    s = set()
    cnt = 0
    if mid == 0:
        return True
    for i in range(n):
        if arr[i] < mid:
            s.add(arr[i])
        if len(s) == mid:
            cnt += 1
            if cnt == k:
                return True
            s.clear()
    return False

for _ in range(int(input())):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    s = set(arr)
    m = 0
    while m in s:
        m += 1
    left, right = 0, m
    ans = 0
    while left <= right:
        mid = left + (right - left) // 2
        if not solve(arr, n, k, mid):
            right = mid - 1
        else:
            ans = mid
            left = mid + 1
    print(ans)