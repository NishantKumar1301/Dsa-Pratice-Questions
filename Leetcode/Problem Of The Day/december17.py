#Question : Final Array State After K Multiplication Operations I
#Link to the question: https://leetcode.com/problems/final-array-state-after-k-multiplication-operations-i/description/?envType=daily-question&envId=2024-12-17
from heapq import heappush , heappop
class Solution(object):
    def getFinalState(self, nums, k, multiplier):
        """
        :type nums: List[int]
        :type k: int
        :type multiplier: int
        :rtype: List[int]
        """
        pq =[]
        for idx, value in enumerate(nums):
            heappush(pq,(value,idx))
        
        for i in range(k):
            min_element_idx = heappop(pq)[1]
            nums[min_element_idx]*= multiplier
            heappush(pq,(nums[min_element_idx],min_element_idx))

        return nums
