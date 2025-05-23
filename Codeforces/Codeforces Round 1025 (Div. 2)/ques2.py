#Question : Slice to Survive
#Link to the question: https://codeforces.com/contest/2109/problem/B

# Contest: Codeforces Round 1025 (Div. 2)
# Date: May 17, 2025
# Author: Nishant Kumar

def solve1(t, p):
    ans = 0
    m = 2
    while t > 1:
        t = (t + m - 1) // m
        ans += 1
    while p > 1:
        p = (p + m - 1) // 2
        ans += 1
    return ans

def solve():
        n, m, a, b = map(int, input().split())
        row = min(a, n - a + 1)
        col = min(b, m - b + 1)
        ans1 = solve1(m, row) +1
        ans2 = solve1(n, col)  +1 
        print(min(ans1 , ans2))

if __name__ == "__main__":
    for _ in range(int(input())):
        solve()

# Author: Nishant Kumar



