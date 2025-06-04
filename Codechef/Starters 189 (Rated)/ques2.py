# cook your dish here
#Question : Nutrition Cost
#Link to the question: https://www.codechef.com/START189B/problems/NUTRICOST
for _ in range(int(input())):
    n,c = map(int, input().split())
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))
    mini = [float('inf')] * 101  
    for i in range(n):
        v = arr1[i]
        if arr2[i] < mini[v]:
            mini[v] = arr2[i]
    ans = 0
    for j in range(1, 101):
        if mini[j] != float('inf'):
            p = c - mini[j]
            if p > 0:
                ans += p
    print(ans)