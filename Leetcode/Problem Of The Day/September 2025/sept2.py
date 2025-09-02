#Question : Find the Number of Ways to Place People I
#Link to the question:  https://leetcode.com/problems/find-the-number-of-ways-to-place-people-i/
class Solution(object):
    def numberOfPairs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        n = len(points)
        ans = 0
        for i in range(n):
            x1,y1 = points[i][0],points[i][1]
            for j in range(n):
                if i==j:
                    continue
                x2,y2 = points[j][0],points[j][1]
                if x1<=x2 and y1>=y2:
                    flag = False
                    for k in range(n):
                        if k==i or k==j:
                            continue
                        x3,y3 = points[k][0] , points[k][1]
                        if (x3>=x1 and x3<=x2 and y3<=y1 and y3>=y2):
                            flag = True
                            break
                    if not flag:
                        ans+=1
        return ans
