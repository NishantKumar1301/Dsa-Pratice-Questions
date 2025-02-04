#Question :  Power of Points
#Link to the question: https://codeforces.com/contest/1857/problem/E

def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    
    vp = [(arr[i], i) for i in range(n)]
    vp.sort()  
    
    val = sum(vp[i][0] - vp[0][0] + 1 for i in range(n))
    
    ans = [0] * n
    ans[vp[0][1]] = val  
    for i in range(1, n):
        val -= (n - i) * (vp[i][0] - vp[i - 1][0])
        val += i * (vp[i][0] - vp[i - 1][0])
        ans[vp[i][1]] = val
    
    print(" ".join(map(str, ans)))


for _ in range(int(input())):
    solve()

