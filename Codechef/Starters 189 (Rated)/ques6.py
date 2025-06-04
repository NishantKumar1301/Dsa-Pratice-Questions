#Question : Sortable Subarrays (Easy)
# cook your dish here
#Link to the question: https://www.codechef.com/START189B/problems/SORTSUB7EZ
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        idx = -1  
        for j in range(i, n):
            v= arr[j]
            h=(v - 1) // 2
            if idx < h:
                idx += 1
                ans += 1
            elif idx < v:
                ans += 1
                idx = v
            else:
                break
    print(ans)
