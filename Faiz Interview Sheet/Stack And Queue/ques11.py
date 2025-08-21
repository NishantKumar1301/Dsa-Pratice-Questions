#Question : Sum of Subarray Ranges
#Link to the question: https://leetcode.com/problems/sum-of-subarray-ranges/

class Solution(object):
    def findPreviousSmaller(self,nums):
        n = len(nums)
        pse = [-1]*n
        stack =[]
        for i in range(n):
            while len(stack)>0 and nums[stack[-1]]>=nums[i]:
                stack.pop()
            pse[i]=-1 if len(stack)==0 else stack[-1]
            stack.append(i)
        return pse
    
    def findNextSmaller(self,nums):
        n = len(nums)
        nse = [-1]*n
        stack = []
        for i in range(n-1,-1,-1):
            while len(stack)>0 and nums[stack[-1]]>nums[i]:
                stack.pop()
            nse[i]=n if len(stack)==0 else stack[-1]
            stack.append(i)
        return nse

    def findMinimumSubarraySum(self,nums):
        n = len(nums)
        pse = self.findPreviousSmaller(nums)
        nse = self.findNextSmaller(nums)
        ans = 0
        for i in range(n):
            left = i-pse[i]
            right = nse[i]-i
            total = left*right*nums[i]
            ans+=total
        return ans
    
    def findPreviousGreater(self,nums):
        n = len(nums)
        stack = []
        pge = [-1]*n
        for i in range(n):
            while len(stack)>0 and nums[stack[-1]]<=nums[i]:
                stack.pop()
            pge[i]=-1 if len(stack)==0 else stack[-1]
            stack.append(i)
        return pge
    
    def findNextGreater(self,nums):
        n = len(nums)
        stack = []
        nge = [-1]*n
        for i in range(n-1,-1,-1):
            while len(stack)>0 and nums[stack[-1]]<nums[i]:
                stack.pop()
            nge[i]=n if len(stack)==0 else stack[-1]
            stack.append(i)
        return nge
    
    def findMaximumSubarraySum(self,nums):
        n = len(nums)
        pge = self.findPreviousGreater(nums)
        nge = self.findNextGreater(nums)
        ans = 0
        for i in range(n):
            left = i - pge[i]
            right = nge[i]-i
            total = nums[i]*left*right
            ans+=total
        return ans

    def subArrayRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #Ans  = sumOfMaximumSubArray(nums)-sumOfMinimumSubArray(nums)
        maxSum = self.findMaximumSubarraySum(nums)
        minSum = self.findMinimumSubarraySum(nums)
        print(maxSum)
        print(minSum)
        return maxSum - minSum 
        