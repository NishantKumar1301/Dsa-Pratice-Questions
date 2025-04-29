#Question : Count Subarrays Where Max Element Appears at Least K Times
#Link to the question: https://leetcode.com/problems/count-subarrays-where-max-element-appears-at-least-k-times/description/?envType=daily-question&envId=2025-04-29

class Solution:
    def countSubarrays(self, nums, k):
        maxi = max(nums)
        idx = []
        ans = 0
        for index, element in enumerate(nums):
            if element == maxi:
                idx.append(index)
            freq = len(idx)
            if freq >= k:
                ans += idx[-k] + 1
        return ans

