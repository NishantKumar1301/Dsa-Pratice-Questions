#Question : Minimum Discards to Balance Inventory
#Link to the question: https://leetcode.com/contest/biweekly-contest-165/problems/minimum-discards-to-balance-inventory/
from collections import deque , defaultdict
class Solution(object):
    def minArrivalsToDiscard(self, arrivals, w, m):
        """
        :type arrivals: List[int]
        :type w: int
        :type m: int
        :rtype: int
        """
        freq = defaultdict(int)
        queue = deque()
        ans = 0
        for num in arrivals:
            if len(queue)==w:
                old = queue.popleft()
                if old:
                    freq[old]-=1
                    if freq[old]==0:
                        del freq[old]

            if freq[num]>=m:
                queue.append(None)
                ans+=1
            else:
                freq[num]+=1
                queue.append(num)
        return ans