#Question : Minimize the Maximum Difference of Pairs
#Link to the question: https://leetcode.com/problems/minimize-the-maximum-difference-of-pairs/
class Solution(object):
    def is_valid(self,nums,mid,p):
        i=0
        pairs=0
        n = len(nums)
        while i<n-1:
            if nums[i+1]-nums[i]<=mid:
                pairs+=1
                i+=2
            else:
                i+=1
        return pairs>=p
    def minimizeMax(self, nums, p):
        """
        :type nums: List[int]
        :type p: int
        :rtype: int
        """
        nums.sort()
        left =0
        right = nums[-1]-nums[0]
        ans = float('inf')
        while left<=right:
            mid = left+(right-left)//2
            if self.is_valid(nums,mid,p):
                ans = mid
                right = mid-1
            else:
                left = mid+1
        return ans
        