#Question : Find Resultant Array After Removing Anagrams
#Link to the question: https://leetcode.com/problems/find-resultant-array-after-removing-anagrams/
from collections import Counter


class Solution(object):
    def removeAnagrams(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        n = len(words)
        freq = [Counter(w) for w in words]
        ans = [words[0]]
        for i in range(1, n):
            if freq[i] != freq[i - 1]:
                ans.append(words[i])
        return ans