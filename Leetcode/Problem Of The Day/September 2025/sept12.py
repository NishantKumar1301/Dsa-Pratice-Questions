#Question : Vowels Game in a String
#Link to the question: https://leetcode.com/problems/vowels-game-in-a-string/
class Solution(object):
    def doesAliceWin(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return any(c in "aeiou" for c in s)