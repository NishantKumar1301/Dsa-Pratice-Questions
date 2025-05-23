#Question : Message Route
#Link to the question: https://cses.fi/problemset/task/1667

def dfs(node, adj, visited, parent):
    visited[node] = True
    for neighbor in adj[node]:
        if not visited[neighbor]:
            parent[neighbor] = node
            dfs(neighbor, adj, visited, parent)

def main():
    n, m = map(int, input().split())
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b = map(int, input().split())
        adj[a].append(b)
        adj[b].append(a)
    visited = [False] * (n + 1)
    parent = [0] * (n + 1)
    dfs(1, adj, visited, parent)
    if not visited[n]:
        print("IMPOSSIBLE")
        return
    path = []
    current = n
    while current != 0:
        path.append(current)
        current = parent[current]
    path.reverse()

    print(len(path))
    print(' '.join(map(str, path)))

main()

