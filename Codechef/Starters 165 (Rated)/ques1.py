#Question : Bulk Discount
#Link to the question: https://www.codechef.com/START165B/problems/BDISC

# cook your dish here
from heapq import heapify, heappop

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    heapify(arr)
    ans = 0
    discount = 0
    while arr:
        cost = heappop(arr)
        ans+=max(cost-discount,0)
        discount+=1
    print(ans)
