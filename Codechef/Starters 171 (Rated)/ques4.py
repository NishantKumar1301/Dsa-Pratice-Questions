#Question : Volcanic Eruption
#Link to the question: https://www.codechef.com/problems/VOLCANO

# cook your dish here
import math
from heapq import heappush, heappop

for _ in range(int(input())):
    n, p = map(int, input().split())
    arr = list(map(int, input().split()))

    INT_MAX = 10**18
    ans = [INT_MAX] * n
    pq = []

    for i in range(n):
        if arr[i] == 0:
            ans[i] = 0
            heappush(pq, (0, i))

    dirs = [-1, 1]  

    while pq:
        curr, u = heappop(pq)

        if curr > ans[u]:
            continue

        for dir in dirs: 
            v = u + dir  

            if 0 <= v < n:
                req = 0 if arr[v] == 0 else math.ceil(arr[v] / p)
                new_t = max(curr, req)

                if new_t < ans[v]:
                    ans[v] = new_t
                    heappush(pq, (new_t, v))

    print(*ans)


