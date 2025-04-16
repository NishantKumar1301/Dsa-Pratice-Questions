#Question : Count the Number of Good Subarrays
#Link to the question: https://leetcode.com/problems/count-the-number-of-good-subarrays/?envType=daily-question&envId=2025-04-16

from collections import defaultdict
class Solution:
    def countGood(self, nums, k):
        n = len(nums)
        left = 0
        right = 0
        ans = 0
        freq = defaultdict(int)
        equal_pairs = 0

        while left < n:
            while right < n and equal_pairs < k:
                freq[nums[right]] += 1
                if freq[nums[right]] >= 2:
                    equal_pairs += freq[nums[right]] - 1
                right += 1
            
            if equal_pairs >= k:
                ans += n - right + 1

            freq[nums[left]] -= 1
            if freq[nums[left]] > 0:
                equal_pairs -= freq[nums[left]]
            left += 1

        return ans