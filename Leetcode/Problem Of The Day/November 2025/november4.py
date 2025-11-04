#Question : Find X-Sum of All K-Long Subarrays I
#Link to the question: https://leetcode.com/problems/find-x-sum-of-all-k-long-subarrays-i/
from collections import Counter
class Solution(object):
    def findXSum(self, nums, k, x):
        """
        :type nums: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        n = len(nums)
        ans = list()
        for i in range(n - k + 1):
            cnt = Counter(nums[i : i + k])
            freq = sorted(cnt.items(), key=lambda item: (-item[1], -item[0]))
            tmp = sum(key * value for key, value in freq[:x])
            ans.append(tmp)
        return ans