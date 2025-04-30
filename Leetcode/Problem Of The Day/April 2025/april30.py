#Question : Find Numbers with Even Number of Digits
#Link to the question: https://leetcode.com/problems/find-numbers-with-even-number-of-digits/description/?envType=daily-question&envId=2025-04-30

class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        for num in nums:
            length = len(str(num))
            if length % 2 == 0:
                ans += 1
        return ans