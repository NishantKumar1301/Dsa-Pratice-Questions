#Question : Array Recoloring
#Link to the question: https://codeforces.com/contest/2075/problem/B


def solve():
    n, k = map(int, input().split())
    v = list(map(int, input().split()))
    ans = 0
    
    if k == 1:
        for i in range(n - 1):
            ans = max(ans, v[i] + v[-1])
        for i in range(1, n):
            ans = max(ans, v[0] + v[i])
        print(ans)
    else:
        v.sort()
        for _ in range(k + 1):
            ans += v.pop()
        print(ans)

for _ in range(int(input())):
    solve()

