#Question : Find the Number of Ways to Place People II
#Link to the question: https://leetcode.com/problems/find-the-number-of-ways-to-place-people-ii/
class Solution(object):
    def numberOfPairs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        n = len(points)
        points.sort(key = lambda x:(x[0],-x[1]))
        ans = 0
        for i in range(n):
            x1,y1 = points[i][0],points[i][1]
            y = float('-inf')
            for j in range(i+1,n):
                x2,y2 =points[j][0],points[j][1]
                if y2>y1:
                    continue
                if y2>y:
                    ans+=1
                    y = y2
        return ans