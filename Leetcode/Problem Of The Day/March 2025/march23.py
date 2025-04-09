#Question : Number of Ways to Arrive at Destination
#Link to the question: https://leetcode.com/problems/number-of-ways-to-arrive-at-destination/description/?envType=daily-question&envId=2025-03-23

import heapq

class Solution:
    def countPaths(self, n, roads):
        MOD  = 1000000007

        adj = [[] for _ in range(n)]
        for start, end, time in roads:
            adj[start].append((end, time))
            adj[end].append((start, time))

        pq = [(0, 0)] 
        t = [float("inf")] * n
        ans = [0] * n

        t[0] = 0  
        ans[0] = 1  

        while pq:
            curr_time, curr_node = heapq.heappop(pq)
            if curr_time > t[curr_node]:
                continue

            for ngbr, road_time in adj[curr_node]:
                if curr_time + road_time < t[ngbr]:
                    t[ngbr] = curr_time + road_time
                    ans[ngbr] = ans[curr_node]
                    heapq.heappush(pq, (t[ngbr], ngbr))

                elif curr_time + road_time == t[ngbr]:
                    ans[ngbr] = (ans[ngbr] + ans[curr_node]) % MOD

        return ans[n - 1]
