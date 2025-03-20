#Question : Minimum Cost Walk in Weighted Graph
#Link to the question: https://leetcode.com/problems/minimum-cost-walk-in-weighted-graph/description/?envType=daily-question&envId=2025-03-20
from collections import deque
class Solution:
    def minimumCost(self, n, edges, queries):
        adj = [[] for _ in range(n)]
        for edge in edges:
            adj[edge[0]].append((edge[1], edge[2]))
            adj[edge[1]].append((edge[0], edge[2]))

        visited = [False] * n

        components = [0] * n
        cost = []

        id = 0

        for node in range(n):
            if not visited[node]:
                cost.append(
                    self.helper(
                        node, adj, visited, components, id
                    )
                )
                id += 1

        ans = []
        for query in queries:
            start, end = query

            if components[start] == components[end]:
                ans.append(cost[components[start]])
            else:
                ans.append(-1)

        return ans

    def helper(
        self, source, adj, visited, components, id
    ):
        queue = deque()

        cost = -1

        queue.append(source)
        visited[source] = True

        while queue:
            node = queue.popleft()

            components[node] = id

            for neighbor, weight in adj[node]:
                cost &= weight

                if visited[neighbor]:
                    continue
                visited[neighbor] = True
                queue.append(neighbor)

        return cost

