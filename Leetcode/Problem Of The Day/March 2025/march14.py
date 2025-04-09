#Question : Maximum Candies Allocated to K Children
#Link to the question: https://leetcode.com/problems/maximum-candies-allocated-to-k-children/description/?envType=daily-question&envId=2025-03-14


class Solution:
    def maximumCandies(self, candies, k):
        cnt = 0
        for c in candies:
            cnt = max(cnt, c)

        left = 0
        right = cnt

        while left < right:
            middle = (left + right + 1) // 2

            if self.helper(candies, k, middle):
                left = middle
            else:
                right = middle - 1

        return left

    def helper(self, arr, k, n):
        cnt = 0

        for num in arr:
            cnt += num // n

        return cnt >= k