#Question : Several and the formula
#Link to the question: https://codeforces.com/contest/2085/problem/C

for _ in range(int(input())):
    x,y = map(int,input().split())
    if x==y:
        print(-1)
        continue
    m = max(x,y)
    n = 1
    while n<=m:
        n*=2
    ans = n-m
    print(ans)