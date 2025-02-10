#Question : Skibidus and Slay
#Link to the question: https://codeforces.com/contest/2065/problem/F

from collections import defaultdict

def solve():
    n = int(input())  
    val = list(map(int, input().split()))  
    val.insert(0, 0) 

    adj = defaultdict(list)
    s = ['0'] * n  

    for _ in range(n - 1):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)

        if val[u] == val[v]:
            s[val[u] - 1] = '1'

    for i in range(1, n + 1):
        freq = {}
        for neighbor in adj[i]:
            freq[val[neighbor]] = freq.get(val[neighbor], 0) + 1
            if freq[val[neighbor]] == 2:
                s[val[neighbor] - 1] = '1'

    print("".join(s))

for _ in range(int(input())):
    solve()
