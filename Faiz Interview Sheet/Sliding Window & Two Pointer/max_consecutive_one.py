#Question : Max Consecutive Ones III
#Link to the question: https://leetcode.com/problems/max-consecutive-ones-iii/

class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        Explanation of the approach to this question : 
        https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/?envType=daily-question&envId=2025-08-24
        """
        left=right = maxLength=zeroCnt = 0
        n  = len(nums)
        while right<n:
            if nums[right]==0:
                zeroCnt+=1
            #If we use if condition instead of while the time complexity would be O(n) instead of O(2n)
            #In this simply move the left by 1 and if we encouter 0 then reduce its count if zeroCnt>k
            #In this if zeroCnt > 1 then we dont update the answer by moving the left
            if zeroCnt>k:
                if nums[left]==0:
                    zeroCnt-=1
                left+=1
            win_size = right-left+1
            maxLength = max(maxLength,win_size)
            right+=1
        return maxLength