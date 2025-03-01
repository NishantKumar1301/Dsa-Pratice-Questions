#Question : Apply Operations to an Array
#Link to the question: https://leetcode.com/problems/apply-operations-to-an-array/description/?envType=daily-question&envId=2025-03-01

class Solution(object):
    def applyOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        ans = []
        for i in range(n-1):
            if nums[i]==nums[i+1] :
                nums[i]*=2
                nums[i+1]=0
        for num in nums:
            if num!=0:
                ans.append(num)
        
        while len(ans)<n:
            ans.append(0)
        
        return ans
        

