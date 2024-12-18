#Question : Bulk Discount
#Link to the question: https://www.codechef.com/START165B/problems/BDISC

# cook your dish here
import heapq

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))

    heapq.heapify(arr) 
    ans = 0
    dis = 0
    
    while arr:
        cost = heapq.heappop(arr)
        ans += max(0, cost - dis)
        dis += 1
    
    print(ans)


