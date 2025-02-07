#Question : Find the Number of Distinct Colors Among the Balls
#Link to the question: https://leetcode.com/problems/find-the-number-of-distinct-colors-among-the-balls/?envType=daily-question&envId=2025-02-07

from collections import defaultdict
class Solution(object):
    def queryResults(self, limit, queries):
        """
        :type limit: int
        :type queries: List[List[int]]
        :r type: List[int]
        """
        n = len(queries)
        color_freq= defaultdict(int)
        ball_color ,ans ={},[]
        for i in range(n):
            ball,color = queries[i][0],queries[i][1]
            if ball in ball_color:
                prev_color = ball_color[ball]
                color_freq[prev_color]-=1
                if color_freq[prev_color]==0:
                    del color_freq[prev_color]
            ball_color[ball]=color
            color_freq[color]+=1
            ans.append(len(color_freq))
        return ans

