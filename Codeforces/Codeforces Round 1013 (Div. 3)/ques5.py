#Question : Interesting Ratio
#Link to the question: https://codeforces.com/contest/2091/problem/E

# Contest: Codeforces Round 1013 (Div. 3)
# Date: March 25, 2025
# Author: Nishant Kumar

def helper(limit):
    v = [True] * (limit + 1)
    v[0] = v[1] = False
    prime = []

    for i in range(2, limit + 1):
        if v[i]:
            prime.append(i)
            for j in range(i * i, limit + 1, i):
                v[j] = False
    return prime

def helper1(n, prime):
    cnt = 0
    for p in prime:
        if p > n:
            break
        cnt += n // p
    return cnt

def solve():
    arr = [int(input()) for _ in range(int(input()))]
    maxi = max(arr)
    p = helper(maxi)
    for n in arr:
        ans = helper1(n, p)
        print(ans)
if __name__ == "__main__":
    solve()
# Author: Nishant Kumar

