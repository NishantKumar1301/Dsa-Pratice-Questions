#Question : Earliest Finish Time for Land and Water Rides I
#Link to the question: https://leetcode.com/contest/biweekly-contest-162

class Solution(object):
    def earliestFinishTime(self, landStartTime, landDuration, waterStartTime, waterDuration):
        """
        :type landStartTime: List[int]
        :type landDuration: List[int]
        :type waterStartTime: List[int]
        :type waterDuration: List[int]
        :rtype: int
        """
        n,m = len(landStartTime),len(waterStartTime)
        ans = float('inf')
        
        for i in range(n):
            for j in range(m):
                a = landStartTime[i] + landDuration[i]
                b = max(a, waterStartTime[j])
                total = b + waterDuration[j] 
                ans = min(ans, total)

                c= waterStartTime[j]+waterDuration[j]
                d= max(c,landStartTime[i])
                e = d+ landDuration[i]
                ans = min(ans,e)
        return ans