#Question : Count Symmetric Integers
#Link to the question: https://leetcode.com/problems/count-symmetric-integers/description/?envType=daily-question&envId=2025-04-11

class Solution(object):
    def countSymmetricIntegers(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: int
        """
        ans =0
        for i in range(low,high+1):
            s = str(i)
            n = len(s)
            if n%2==1:
                continue
            mid = n//2
            left_sum = sum(int(s[i]) for i in range(mid))
            right_sum = sum(int(s[i]) for i in range(mid,n))
            if left_sum==right_sum:
                ans+=1
        return ans
        

