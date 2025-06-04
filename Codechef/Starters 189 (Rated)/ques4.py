# cook your dish here
#Question : Number Walks
#Link to the question: https://www.codechef.com/START189B/problems/NUMBERWALK
import bisect
MOD = 10**18
for _ in range(int(input())):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    arr2 = [[] for _ in range(k + 1)]
    res = [MOD] * n
    arr3 = [[] for _ in range(k + 1)]
    for i, val in enumerate(arr):
        arr2[val].append(i)
    for i in range(1, k + 1):
        arr3[i] = [MOD] * len(arr2[i])
    for i in range(len(arr2[k])):
        arr3[k][i] = 0
    for v in range(k - 1, 0, -1):
        nxt_p , nxt_c= arr2[v + 1] , arr3[v + 1]
        m = len(nxt_p)
        left = [0] * m
        left[0] = nxt_c[0] - nxt_p[0]
        for i in range(1, m):
            left[i] = min(left[i - 1], nxt_c[i] - nxt_p[i])
        right = [0] * m
        right[m - 1] = nxt_c[m - 1] + nxt_p[m - 1]
        for i in range(m - 2, -1, -1):
            right[i] = min(right[i + 1], nxt_c[i] + nxt_p[i])
        curr = arr2[v]
        x = [MOD] * len(curr)
        for j, p in enumerate(curr):
            idx = bisect.bisect_left(nxt_p, p)
            ans = MOD
            if idx > 0:
                ans = min(ans, left[idx - 1] + p)
            if idx < m:
                ans = min(ans, right[idx] - p)
            x[j] = ans
        arr3[v] = x
    
    for j, p in enumerate(arr2[1]):
        res[p] = arr3[1][j]
    for i in range(1, n):
        res[i] = min(res[i], res[i - 1] + 1)
    for i in range(n - 2, -1, -1):
        res[i] = min(res[i], res[i + 1] + 1)
    print(" ".join(map(str, res)))


