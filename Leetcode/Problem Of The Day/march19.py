#Question : Minimum Operations to Make Binary Array Elements Equal to One I
#Link to the question: https://leetcode.com/problems/minimum-operations-to-make-binary-array-elements-equal-to-one-i/description/?envType=daily-question&envId=2025-03-19

class Solution:
    def minOperations(self, nums):
        ans = 0
        for i in range(2, len(nums)):

            if nums[i - 2] == 0:
                ans += 1
                nums[i - 2] = nums[i - 2] ^ 1
                nums[i - 1] = nums[i - 1] ^ 1
                nums[i] = nums[i] ^ 1

        if sum(nums) == len(nums):
            return ans
        return -1