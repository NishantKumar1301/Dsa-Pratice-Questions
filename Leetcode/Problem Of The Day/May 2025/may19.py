#Question : Type of Triangle
#Link to the question: https://leetcode.com/problems/type-of-triangle/description/?envType=daily-question&envId=2025-05-19

class Solution(object):
    def triangleType(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        nums.sort()
        ans = ""
        if nums[0]+nums[1]>nums[2]:
            if nums[0]==nums[1]==nums[2]:
                ans = "equilateral"
            elif nums[0]==nums[1] or nums[1]==nums[2] or nums[2]==nums[0]:
                ans = "isosceles"
            else :
                ans = "scalene"
        else:
            ans = "none"
        return ans




