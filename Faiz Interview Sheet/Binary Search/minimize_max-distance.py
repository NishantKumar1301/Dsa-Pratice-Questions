#Question : Minimize Max Distance to Gas Station
#Link to the question: https://www.geeksforgeeks.org/problems/minimize-max-distance-to-gas-station/1
from heapq import heappush, heappop
class Solution:
    def minMaxDist(self, stations, k):
        n = len(stations)
        if n <= 1:
            return 0.0
        
        howMany = [0] * (n - 1)
        pq = []
        for i in range(n - 1):
            heappush(pq, (-1 * (stations[i + 1] - stations[i]), i))
        for _ in range(k):
            diff, idx = heappop(pq)
            howMany[idx] += 1
            diff = stations[idx + 1] - stations[idx]
            new_len = diff / (howMany[idx] + 1)
            heappush(pq, (-1 * new_len, idx))
        return pq[0][0] * (-1)