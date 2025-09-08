#Question :  Convert Integer to the Sum of Two No-Zero Integers
#Link to the question: https://leetcode.com/problems/convert-integer-to-the-sum-of-two-no-zero-integers/
class Solution(object):
    def getNoZeroIntegers(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        for i in range(1,n):
            left = i
            right = n-i
            if '0' not in str(left) and '0' not in str(right):
                return [left,right]
        return []