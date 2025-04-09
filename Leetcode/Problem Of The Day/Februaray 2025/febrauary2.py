#Question : Check if Array Is Sorted and Rotated
#Link to the question: https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/description/?envType=daily-question&envId=2025-02-02


class Solution(object):
    def check(self, nums):
        n = len(nums)
        if n <=1:
            return True
        count =0
        for i in range(1,n):
            if nums[i]<nums[i-1]:
                count+=1
        if nums[0]<nums[n-1]:
            count+=1
        return count<=1
        

