#Question : Find Minimum Time to Reach Last Room I
#Link to the question: https://leetcode.com/problems/find-minimum-time-to-reach-last-room-i/description/?envType=daily-question&envId=2025-05-07


from collections import heapq
class Solution(object):
    def minTimeToReach(self, moveTime):
        """
        :type moveTime: List[List[int]]
        :rtype: int
        """
        n =len(moveTime)
        m = len(moveTime[0])
        dist = [[float('inf')] * m for _  in range(n)]
        dist[0][0] = 0
        #Priority pqeue: (time, x, y)
        pq = [(0, 0, 0)]
        dirs = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        while pq:
            t, x, y = heapq.heappop(pq)
            if x == n-1 and y == m-1:
                return t
            for dx, dy in dirs:
                new_x = x + dx
                new_y = y + dy
                if 0 <= new_x < n and 0 <= new_y < m:
                    diff = max(t, moveTime[new_x][new_y]) + 1
                    if diff < dist[new_x][new_y]:
                        dist[new_x][new_y] = diff
                        heapq.heappush(pq, (diff, new_x, new_y))
        return -1                