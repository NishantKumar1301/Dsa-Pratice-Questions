#Question : Maximum Erasure Value
#Link to the question: https://leetcode.com/problems/maximum-erasure-value/

class Solution(object):
    def maximumUniqueSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = right = s = 0
        freq,n, maxi = {},len(nums),float('-inf')
        while right<n:
            if nums[right] in freq:
                del freq[nums[left]]
                s-=nums[left]
                left+=1
            else:
                s+=nums[right]
                freq[nums[right]]=True
                right+=1
                maxi = max(maxi,s)
        return maxi