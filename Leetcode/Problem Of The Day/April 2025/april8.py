#Question : Minimum Number of Operations to Make Elements in Array Distinct
#Link to the question: https://leetcode.com/problems/minimum-number-of-operations-to-make-elements-in-array-distinct/description/?envType=daily-question&envId=2025-04-08

class Solution(object):
    def minimumOperations(self, nums):
        ans = 0
        while len(nums) > len(set(nums)):
            nums = nums[3:]  
            ans += 1
        return ans
        

