#Question : Expected Median
#Link to the question: https://codeforces.com/contest/1999/problem/F


MOD = int(1e9 + 7)
N = int(1e6)

def power_mod_n(x, n):
    x %= MOD
    if n == 0:
        return 1
    elif n == 1:
        return x
    p = power_mod_n((x * x) % MOD, n // 2)
    return (p * x) % MOD if n % 2 else p

def divisor_mod_n(p, q):
    return (p % MOD) * power_mod_n(q, MOD - 2) % MOD

fact = [1] * N
for i in range(1, N):
    fact[i] = fact[i - 1] * i % MOD

def ncr(n, r):
    if r > n:
        return 0
    return divisor_mod_n(fact[n], fact[n - r] * fact[r] % MOD)

def solve():
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    
    cnt1 = arr.count(1)
    cnt0 = n - cnt1
    req = k // 2 + 1
    
    if cnt1 < req:
        print(0)
        return
    
    ans = 0
    for i in range(req, min(k, cnt1) + 1):
        ans = (ans + ncr(cnt1, i) * ncr(cnt0, k - i) % MOD) % MOD
    
    print(ans)

def main():
    for _ in range(int(input())):
        solve()

if __name__ == "__main__":
    main()
