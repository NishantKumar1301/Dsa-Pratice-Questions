#Question : Sort Colors
#Link to the question: https://leetcode.com/problems/sort-colors/description/?envType=daily-question&envId=2025-05-17

class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :returnType: None Do not return anything, modify nums in-place instead.
        """
        n,zero,one = len(nums),0,0
        for num in nums:
            if num==0:
                zero+=1
            elif num==1:
                one+=1
        for i in range(zero):
            nums[i]=0
        for i in range(zero,one+zero):
            nums[i]=1
        for i in range(one+zero,n):
            nums[i]=2