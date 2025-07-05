#Question : Minimum Cost Path with Alternating Directions II
#Link to the question:  https://leetcode.com/contest/biweekly-contest-160/problems/minimum-cost-path-with-alternating-directions-ii/

from heapq import heappush , heappop
INF = 4*10**18
class Solution(object):
    
    def get_id(self,i,j,n):
        return i*n + j
        
    def minCost(self, m, n, waitCost):
        """
        :type m: int
        :type n: int
        :type waitCost: List[List[int]]
        :rtype: int
        """
        dist = [INF] * (m * n * 2)
        dist[1] = 1
        pq = [(1, 0, 1)]  # (cost, id, p)
        dx, dy = [1, 0], [0, 1]

        while pq:
            cost, id, p = heappop(pq)
            if cost != dist[id * 2 + p]:
                continue
            i,j = id // n, id % n
            if i == m - 1 and j == n - 1:
                return cost
            if p == 1:
                for k in range(2):
                    new_i, new_j = i + dx[k], j + dy[k]
                    if new_i >= m or new_j >= n:
                        continue
                    new_id = self.get_id(new_i, new_j, n)
                    new_cost = cost + (new_i + 1) * (new_j + 1)
                    if new_cost < dist[new_id * 2]:
                        dist[new_id * 2] = new_cost
                        heappush(pq, (new_cost, new_id, 0))
            else:
                new_cost = cost + waitCost[i][j]
                if new_cost < dist[id * 2 + 1]:
                    dist[id * 2 + 1] = new_cost
                    heappush(pq, (new_cost, id, 1))

        return -1