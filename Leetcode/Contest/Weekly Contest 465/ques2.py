class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxi,ans = max(nums),0
        c = max(1, maxi.bit_length())   
        d = 1 << c
        e = d - 1
        dp = [-1] * d
        for x in nums:
            dp[x] = max(dp[x], x)
        for b in range(c):
            for m in range(d):
                if (1 << b) & m:
                    dp[m] = max(dp[m], dp[m ^ (1 << b)])
        ans = 0
        for x in nums:
            y = dp[e ^ x]
            if y != -1:
                ans = max(ans, x * y)
        return ans
