#Question : Kevin and Numbers
#Link to the question: https://codeforces.com/contest/2061/problem/D


"""Author : Nishant Kumar"""

from collections import deque
from heapq import heapify, heappush, heappop


def solve():
    n, m = map(int, input().split())
    arr1 = deque(sorted(map(int, input().split()), reverse=True))
    arr2 = list(map(int, input().split()))
    
    if sum(arr1) != sum(arr2) or m > n:
        print("NO")
        return

    arr2 = [-x for x in arr2]
    heapify(arr2)

    while arr2:
        if not arr1 or len(arr2) > len(arr1):
            print("NO")
            return

        largest_b = -heappop(arr2)

        if arr1[0] > largest_b:
            print("NO")
            return

        if arr1[0] == largest_b:
            arr1.popleft()
        else:
            heappush(arr2, -(largest_b // 2))
            heappush(arr2, -((largest_b + 1) // 2))

    print("YES")


for _ in range(int(input())):
    solve()

"""Author : Nishant Kumar"""

