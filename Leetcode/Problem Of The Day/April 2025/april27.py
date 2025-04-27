#Question : Count Subarrays of Length Three With a Condition
#Link to the question: https://leetcode.com/problems/count-subarrays-of-length-three-with-a-condition/description/?envType=daily-question&envId=2025-04-27

class Solution(object):
    def countSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        ans = 0
        for i in range(1,n-1):
            if nums[i]==(nums[i-1]+nums[i+1])*2:
                ans +=1
        return ans

