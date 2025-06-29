#Question : Number of Subsequences That Satisfy the Given Sum Condition
#Link to the question:  https://leetcode.com/problems/number-of-subsequences-that-satisfy-the-given-sum-condition/

MOD = 10**9+7
class Solution(object):
    def power_of_two(self,n):
        arr = [1]*n
        for i in range(1,n):
            arr[i]=(arr[i-1]*2)%MOD
        return arr

    def numSubseq(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        power_2 = self.power_of_two(n)
        nums.sort()
        left,right = 0,n-1
        ans =0
        while left<=right:
            if nums[left]+nums[right]>target:
                right-=1
            else :
                ans= (ans+power_2[right-left])%MOD
                left+=1
        return ans
        
        