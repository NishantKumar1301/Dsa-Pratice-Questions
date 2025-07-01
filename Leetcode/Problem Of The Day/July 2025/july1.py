#Question : Find the Original Typed String I
#Link to the question: https://leetcode.com/problems/find-the-original-typed-string-i/

class Solution(object):
    def possibleStringCount(self, word):
        """
        :type word: str
        :rtype: int
        """
        n, ans = len(word), 1
        for i in range(1, n):
            if word[i - 1] == word[i]:
                ans += 1
        return ans
        