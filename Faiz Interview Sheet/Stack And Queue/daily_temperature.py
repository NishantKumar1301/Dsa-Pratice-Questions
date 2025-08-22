#Question : Daily Temperatures
#Link to the question: https://leetcode.com/problems/daily-temperatures/
class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        n = len(temperatures)
        ans = [-1]*n
        stack = []
        for i in range(n-1,-1,-1):
            while len(stack)>0 and temperatures[i]>=temperatures[stack[-1]]:
                stack.pop()
            ans[i]=stack[-1]-i if len(stack)>0 else 0
            stack.append(i)
        return ans
