#Question : Subarrays with K Different Integers
#Link to the question: https://leetcode.com/problems/subarrays-with-k-different-integers/
class Solution(object):
    def helper(self,nums,k):
        left = right = cnt = 0
        freq = {}
        n = len(nums)
        while right<n:
            if nums[right] in freq:
                freq[nums[right]]+=1
            else:
                freq[nums[right]]=1
            while len(freq)>k:
                freq[nums[left]]-=1
                if freq[nums[left]]==0:
                    del freq[nums[left]]
                left+=1
            if len(freq)<=k:
                cnt+=(right-left+1)
            right+=1
        return cnt

    def subarraysWithKDistinct(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        ans = self.helper(nums,k)-self.helper(nums,k-1)
        return ans