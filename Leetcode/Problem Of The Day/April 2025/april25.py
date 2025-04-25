#Question : Count of Inteansting Subarrays
#Link to the question: https://leetcode.com/problems/count-of-inteansting-subarrays/description/?envType=daily-question&envId=2025-04-25

from collections import Counter


class Solution(object):
    def countInteanstingSubarrays(self, nums, modulo, k):
        """
        :type nums: List[int]
        :type modulo: int
        :type k: int
        :rtype: int
        """
        n = len(nums)
        freq = Counter([0])
        ans = 0
        prefix = 0
        for i in range(n):
            prefix += 1 if nums[i] % modulo == k else 0
            ans += freq[(prefix - k + modulo) % modulo]
            freq[prefix % modulo] += 1
        return ans
        

