#Question : Smallest Subarrays With Maximum Bitwise OR
#Link to the question: https://leetcode.com/problems/smallest-subarrays-with-maximum-bitwise-or/
class Solution(object):
    def smallestSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        ans = [0]*n
        setbit = [-1]*32
        for i in range(n-1,-1,-1):
            lastIdx = i
            #Check whether the jth bit of nums[i] is set or not of the 32 bit form
            for j in range(32):
                if not (nums[i] & (1<<j)):
                    #If jth bit is not set : make last = max(last,setbit[j])
                    if setbit[j]!=-1:
                        lastIdx = max(lastIdx,setbit[j])
                #If it is already set then update the setbit
                else:
                    setbit[j]=i
            ans[i]=lastIdx-i+1
        return ans