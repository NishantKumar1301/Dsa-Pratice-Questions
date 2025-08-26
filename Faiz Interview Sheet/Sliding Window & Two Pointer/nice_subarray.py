#Question : Count Number of Nice Subarrays
#Link to the question: https://leetcode.com/problems/count-number-of-nice-subarrays/
class Solution(object):
    def helper(self,nums,k):
        n = len(nums)
        left=right=cnt=sum_=0
        if k<0:
            return 0
        while right<n:
            #Instead of doing sum of element do the sum of its modulo 
            # sum_+=nums[right]
            sum_+=(nums[right]%2)
            while sum_>k:
                sum_-= (nums[left]%2)
                left+=1
            cnt+=right-left+1
            right+=1
        return cnt
    
    def numberOfSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        #Hint : Convert the array to binary array of 0 & 1 , 1 indicates number = odd 
        #Then the question reduced to find the number of subarray whose sum==k
        n = len(nums)
        # arr = [-1]*n
        # for i , num in enumerate(nums):
        #     if num%2==1:
        #         arr[i]=1
        #     else:
        #         arr[i]=0
        # ans = self.helper(arr,k)-self.helper(arr,k-1)
        ans = self.helper(nums,k)-self.helper(nums,k-1)
        return ans  #This takes an O(n) memory , so its better to pass the nums itself, and while doing sum of element , find the sum of modulo 2
        