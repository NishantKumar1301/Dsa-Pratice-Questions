#Question : Find X-Sum of All K-Long Subarrays I
#Link to the question: https://leetcode.com/problems/find-x-sum-of-all-k-long-subarrays-i/
from heapq import heappush , heappop
from collections import Counter
class Solution(object):
    def findMaxXSum(self,mp,x):
        pq = []
        for num,freq in mp.items():
            heappush(pq,(freq,num))
            if len(pq)>x:
                heappop(pq)
        sum_val = 0
        while pq:
            freq,num = heappop(pq)
            sum_val+=freq*num
        return sum_val

    def findXSum(self, nums, k, x):
        """
        :type nums: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        n = len(nums)
        ans = []
        mp = Counter()
        i =0
        for j in range(n):
            mp[nums[j]]+=1
            if j-i+1==k:
                ans.append(self.findMaxXSum(mp,x))
                mp[nums[i]]-=1
                if mp[nums[i]]==0:
                    del mp[nums[i]]
                i+=1
        return ans