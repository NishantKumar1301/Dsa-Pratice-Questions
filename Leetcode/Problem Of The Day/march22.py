#Question : Count the Number of Complete Components
#Link to the question: https://leetcode.com/problems/count-the-number-of-complete-components/?envType=daily-question&envId=2025-03-22

from collections import defaultdict
class Solution:
    def countCompleteComponents(self, n, edges):
        graph = [[] for _ in range(n)]
        freq = defaultdict(int)

        for vertex in range(n):
            graph[vertex] = [vertex]

        for v1, v2 in edges:
            graph[v1].append(v2)
            graph[v2].append(v1)

        for vertex in range(n):
            neighbors = tuple(sorted(graph[vertex]))
            freq[neighbors] += 1

        return sum(
            1
            for neighbors, freq in freq.items()
            if len(neighbors) == freq
        )


