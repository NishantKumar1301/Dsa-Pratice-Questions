#Question : Longest Unequal Adjacent Groups Subsequence I
#Link to the question: https://leetcode.com/problems/longest-unequal-adjacent-groups-subsequence-i/description/?envType=daily-question&envId=2025-05-15

class Solution(object):
    def getLongestSubsequence(self, words, groups):
        """
        :type words: List[str]
        :type groups: List[int]
        :rtype: List[str]
        """
        ans = []
        for i in range(len(words)):
            if i==0 or (groups[i]!=groups[i-1]):
                ans.append(words[i])
        return ans
