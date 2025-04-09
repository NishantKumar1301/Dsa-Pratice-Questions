#Question : Minimum Operations to Exceed Threshold Value II
#Link to the question: https://leetcode.com/problems/minimum-operations-to-exceed-threshold-value-ii/description/?envType=daily-question&envId=2025-02-13


from heapq import heapify,heappop,heappush
class Solution(object):
    def minOperations(self, nums, k):
        heapify(nums)
        ans =0
        while nums:
            mini1 = heappop(nums)
            if mini1>=k:
                break
            mini2 = heappop(nums)
            val = min(mini1,mini2)*2+max(mini2,mini1)
            heappush(nums,val)
            ans+=1
        return ans