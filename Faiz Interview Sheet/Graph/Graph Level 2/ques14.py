#Question : Bus Routes
#Link to the question:  https://leetcode.com/problems/bus-routes/

from collections import deque, defaultdict

class Solution:
    def numBusesToDestination(self, routes, source, target):
        if source == target:
            return 0
        adj = defaultdict(list)
        for r, route in enumerate(routes):
            for stop in route:
                adj[stop].append(r)
        q = deque()
        visited = set()
        for route in adj[source]:
            q.append(route)
            visited.add(route)
        ans = 1
        while q:
            for _ in range(len(q)):
                route = q.popleft()
                for stop in routes[route]:
                    if stop == target:
                        return ans
                    for next_route in adj[stop]:
                        if next_route not in visited:
                            visited.add(next_route)
                            q.append(next_route)
            ans += 1
        return -1
