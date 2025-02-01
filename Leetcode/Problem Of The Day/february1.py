#Question : Special Array I
#Link to the question: https://leetcode.com/problems/special-array-i/description/?envType=daily-question&envId=2025-02-01


class Solution(object):
    def is_special(self, num1, num2):
        return (num1 % 2 == 0 and num2 % 2 != 0) or (num1 % 2 != 0 and num2 % 2 == 0)

    def isArraySpecial(self, nums):
        n = len(nums)
        for i in range(1, n):
            if not self.is_special(nums[i - 1], nums[i]): 
                return False
        return True
