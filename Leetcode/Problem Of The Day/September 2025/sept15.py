#Question : Maximum Number of Words You Can Type
#Link to the question: https://leetcode.com/problems/maximum-number-of-words-you-can-type
class Solution(object):
    def canBeTypedWords(self, text, brokenLetters):
        """
        :type text: str
        :type brokenLetters: str
        :rtype: int
        """
        ans = 0
        t = text.split()
        for word in t:
            for letter in brokenLetters:
                if letter in word:
                    break
            else:
                ans+=1
        return ans