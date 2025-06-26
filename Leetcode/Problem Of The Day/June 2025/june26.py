#Question : Longest Binary Subsequence Less Than or Equal to K
#Link to the question:  https://leetcode.com/problems/longest-binary-subsequence-less-than-or-equal-to-k/

class Solution(object):
    def longestSubsequence(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        sm = 0
        ans = 0
        bits = k.bit_length()
        for i, ch in enumerate(s[::-1]):
            if ch == "1":
                if i < bits and sm + (1 << i) <= k:
                    sm += 1 << i
                    ans += 1
            else:
                ans += 1
        return ans
        