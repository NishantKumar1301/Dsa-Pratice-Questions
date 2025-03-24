#Question : Remove Duplicates from Sorted Array
#Link to the question: https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/?envType=study-plan-v2&envId=top-interview-150

class Solution(object):
    def removeDuplicates(self, nums):
        k = 1 # unique element =1 
        n = len(nums)
        for i in range(1,n):
            if nums[i]!=nums[i-1]:
                nums[k]=nums[i]
                k+=1
        return k
