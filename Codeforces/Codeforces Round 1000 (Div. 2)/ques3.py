#Question : Remove Exactly Two
#Link to the question: https://codeforces.com/contest/2063/problem/C


# Contest: Codeforces Round 1000 (Div. 2)
# Date: 22-Jan-2025
# Author: Nishant Kumar

def solve():
    n = int(input())
    degrees = [0] * (n + 1)
    edges = set()
    
    for _ in range(n - 1):
        a, b = map(int, input().split())
        degrees[a] += 1
        degrees[b] += 1
        edges.add((a, b))
        edges.add((b, a))
    
    nodes = [(degrees[i], i) for i in range(1, n + 1)]
    nodes.sort(reverse=True) 

    ans = 0

    for i in range(len(nodes)):
        for j in range(i + 1, len(nodes)):
            u, v = nodes[i][1], nodes[j][1]
            if (u, v) not in edges:
                ans = max(ans, nodes[i][0] + nodes[j][0] - 1)
                break

    for u, v in edges:
        ans = max(ans, degrees[u] + degrees[v] - 2)

    print(ans)


if __name__ == "__main__":
    for _ in range(int(input())):
        solve()
