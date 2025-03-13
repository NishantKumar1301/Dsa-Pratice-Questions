#Question : Zero Array Transformation II
#Link to the question: https://leetcode.com/problems/zero-array-transformation-ii/description/?envType=daily-question&envId=2025-03-13

class Solution:
    def minZeroArray(self, nums, queries):
        n = len(nums)
        left, right = 0, len(queries)

        if not self.can_form_zero_array(nums, queries, right):
            return -1

        while left <= right:
            middle = left + (right - left) // 2
            if self.can_form_zero_array(nums, queries, middle):
                right = middle - 1
            else:
                left = middle + 1

        return left

    def can_form_zero_array(
        self, nums, queries, k
    ):
        n = len(nums)
        total = 0
        diff = [0] * (n + 1)

        for i in range(k):
            start, end, val = queries[i]

            diff[start] += val
            diff[end + 1] -= val

        for i in range(n):
            total += diff[i]
            if total < nums[i]:
                return False
        return True