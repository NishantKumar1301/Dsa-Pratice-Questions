#Question : Distinct Arrays
#Link to the question: https://www.codechef.com/START186B/problems/DISTARR

MOD = 998244353
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    ans = 1
    for i in range(n):
        p = arr[i] - i
        if p <= 0:
            ans = 0
            break
        ans = ((ans) * (p % MOD)) % MOD
    print(ans)

