#Question : House Robber IV
#Link to the question: https://leetcode.com/problems/house-robber-iv/description/?envType=daily-question&envId=2025-03-15


class Solution:
    def minCapability(self, nums, k):
        left, right = 1, max(nums)
        total = len(nums)

        while left < right:
            mid = (left + right) // 2
            p = 0

            idx = 0
            while idx < total:
                if nums[idx] <= mid:
                    p += 1
                    idx += 2 
                else:
                    idx += 1

            if p >= k:
                right = mid
            else:
                left = mid + 1

        return left

