#Question : Strong Vertices
#Link to the question: https://codeforces.com/contest/1857/problem/D

for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    c=[]
    for i in range(n):
        c.append(a[i]-b[i])
    maxi = max(c)
    ans = [i+1 for i in range(n) if c[i]==maxi]
    print(len(ans))
    print(*ans)
