#Question : Boneca Ambalabu
#Link to the question: https://codeforces.com/contest/2094/problem/E

# Contest: Codeforces Round 1017 (Div. 4)
# Date: April 13, 2025
# Author: Nishant Kumar

def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    freq = [0] * 30  
    for i in range(n):
        for b in range(len(freq)):
            if arr[i] & (1 << b):
                freq[b] += 1
    ans = 0
    for i in range(n):
        total = 0
        for b in range(30):
            if arr[i] & (1 << b):
                total += (n - freq[b]) * (1 << b)
            else:
                total += freq[b] * (1 << b)
        ans = max(ans, total)
    print(ans)


if __name__ == "__main__":
    for _ in range(int(input())):
        solve()

# Author: Nishant Kumar


