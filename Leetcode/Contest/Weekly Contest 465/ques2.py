#Question : Maximum Product of Two Integers With No Common Bits
#Link to the question: https://leetcode.com/contest/weekly-contest-465/problems/maximum-product-of-two-integers-with-no-common-bits/
class Solution:
    def maxProduct(self, nums):
        maxi , ans  = max(nums) , 0
        n = max(1, maxi.bit_length())
        m = 1 << n
        p = m - 1
        dp = [-1] * m
        for num in nums:
            dp[num] = max(dp[num], num)
        for i in range(n):
            for j in range(m):
                if j & (1 << i):
                    dp[j] = max(dp[j], dp[j ^ (1 << i)])
        for num in nums:
            arr = dp[p ^ num]
            if arr != -1:
                ans = max(ans, num * arr)
        return ans
