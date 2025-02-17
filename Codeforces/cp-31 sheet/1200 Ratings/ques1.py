#Question : Same Differences
#Link to the question: https://codeforces.com/problemset/problem/1520/D

from collections import defaultdict
def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    # Write your logic here
    ans =0
    freq = defaultdict(int)
    for i in range(n):
        ans += freq[arr[i]-i]
        freq[arr[i]-i]+=1
    print(ans)


if __name__ == "__main__":
    for _ in range(int(input())):
        solve()


