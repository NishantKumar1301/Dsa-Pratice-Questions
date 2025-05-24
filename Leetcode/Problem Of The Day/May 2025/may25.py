#Question : Find Words Containing Character
#Link to the question: https://leetcode.com/problems/find-words-containing-character/?envType=daily-question&envId=2025-05-24

class Solution(object):
    def findWordsContaining(self, words, x):
        """
        :type words: List[str]
        :type x: str
        :rtype: List[int]
        """
        ans = []
        for i in range(len(words)):
            if x in words[i]:
                ans.append(i)
        return ans        