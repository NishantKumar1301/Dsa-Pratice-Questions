#Question : Assembly via Minimums
#Link to the question: https://codeforces.com/contest/1857/problem/C


from collections import Counter

def solve():
    n = int(input().strip())
    m = (n * (n - 1)) // 2
    arr = list(map(int, input().split()))

    arr.sort()

    if arr[0] == arr[m-1]:
        print(" ".join(map(str, [arr[0]] * n)))
        return

    freq = Counter(arr)
    ans = []

    for num, cnt in sorted(freq.items()):
        while cnt >= n - (len(ans) + 1):
            cnt -= n - (len(ans) + 1)
            ans.append(num)
            if len(ans) == n:
                print(" ".join(map(str, ans)))
                return

for _ in range(int(input())):
    solve()
