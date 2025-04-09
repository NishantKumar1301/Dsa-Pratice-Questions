#Question : Min Max MEX
#Link to the question: https://codeforces.com/contest/2093/problem/E

def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    lo, hi = 0, n
    ans = 0
    while lo <= hi:
        mid = (lo + hi) // 2
        cnt = 0
        cur = 0
        vis = [False] * (mid + 1)
        for i in range(n):
            if a[i] < mid and not vis[a[i]]:
                vis[a[i]] = True
                cur += 1
            if cur == mid:
                cnt += 1
                cur = 0
                vis = [False] * (mid + 1)
        if cnt >= k:
            ans = mid
            lo = mid + 1
        else:
            hi = mid - 1
    print(ans)

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline
    for _ in range(int(input())):
        solve()
