#Question : Find N Unique Integers Sum up to Zero
#Link to the question: https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero/
class Solution(object):
    def sumZero(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        ans = []
        for i in range(1,n//2+1):
            ans.append(i)
            ans.append(-i)
        if n % 2==1:
            ans.append(0)
        return ans