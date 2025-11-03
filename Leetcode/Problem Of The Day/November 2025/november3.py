#Question : Minimum Time to Make Rope Colorful
#Link to the question: https://leetcode.com/problems/minimum-time-to-make-rope-colorful/
class Solution(object):
    def minCost(self, colors, neededTime):
        """
        :type colors: str
        :type neededTime: List[int]
        :rtype: int
        """
        n = len(colors)
        ans = prev = 0
        for i in range(n):
            curr = neededTime[i]
            if i>0 and colors[i] != colors[i-1]:
                prev =0
            ans+=min(prev,curr)
            prev = max(prev,curr)
        return ans