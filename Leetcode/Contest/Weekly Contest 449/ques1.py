#Question : Minimum Deletions for At Most K Distinct Characters
#Link to the question: https://leetcode.com/contest/weekly-contest-449/problems/minimum-deletions-for-at-most-k-distinct-characters/description/
from collections import Counter
class Solution(object):
    def minDeletion(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        # s= set(s)
        # return len(s)-k
        freq = Counter(s)
        freq = sorted(freq.values())
        ans = 0
        n = len(freq) - k
        for i in range(n):
            ans += freq[i]
        return ans
