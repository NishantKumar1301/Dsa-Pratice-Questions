#Question : Maximum Number of Events That Can Be Attended II
#Link to the question:  https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended-ii/

from bisect import bisect_right
class Solution(object):
    def solve(self,events,idx,k,n,dp,start):
        if idx>=n or k<=0:
            return 0

        if dp[idx][k]!=-1:
            return  dp[idx][k]
        
        val = events[idx][2]
        
        j = bisect_right(start,events[idx][1])

        not_take = self.solve(events,idx+1,k,n,dp,start)
        # j = n
        # for p in range(idx+1,n):
        #     if events[p][0]>events[idx][1]:  # Linear search gives tle 
        #         j = p
        #         break
        take = val + self.solve(events,j,k-1,n,dp,start)
        dp[idx][k]= max(take,not_take)
        return dp[idx][k]

    def maxValue(self, events, k):
        """
        :type events: List[List[int]]
        :type k: int
        :rtype: int
        """
        events.sort(key = lambda x : x[0])
        n = len(events)
        #Create a dp of size (n+1)[k+1]
        dp = [[-1]*(k+1) for _ in range(n+1)]
        start = [event[0] for event in events]
        ans = self.solve(events,0,k,n,dp,start)
        return ans