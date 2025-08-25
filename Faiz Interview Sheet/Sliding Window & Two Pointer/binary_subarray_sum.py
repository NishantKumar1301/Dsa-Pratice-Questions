#Question : Binary Subarrays With Sum
#Link to the question: https://leetcode.com/problems/binary-subarrays-with-sum/

class Solution(object):
    def numSubarraysWithSum(self, nums, goal):
        """
        :type nums: List[int]
        :type goal: int
        :rtype: int
        """
        #Method 1 : This will take O(n) space complexity
        # prefix_sum = 0
        # mp = {}
        # mp[0]=1
        # ans=0
        # n = len(nums)
        # for i in range(n):
        #     prefix_sum+=nums[i]
        #     if prefix_sum-goal in mp:
        #         ans+=mp[prefix_sum-goal]
        #     if prefix_sum in mp:
        #         mp[prefix_sum]+=1
        #     else:
        #         mp[prefix_sum]=1
        # return ans

        #Method 2 : Using sliding window : this will take O(1) memory
        #Subarray sum == k = sumArraySum(<=k)-subArraySum(<=k-1)
        ans = self.helper(nums,goal)-self.helper(nums,goal-1)
        return ans
    
    def helper(self,nums,k):
        if k<0:
            return 0
        left = right = cnt = sum_=0
        n = len(nums)
        while right<n:
            sum_+=nums[right]
            while sum_>k:
                sum_-=nums[left]
                left+=1
            cnt+=(right-left+1)
            right+=1
        return cnt