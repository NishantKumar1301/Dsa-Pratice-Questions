#Question : Valid Word
#Link to the question: https://leetcode.com/problems/valid-word/

class Solution(object):
    def isValid(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if len(word) < 3:
            return False

        vowel = False
        consonant = False

        for c in word:
            if c.isalpha():
                if c.lower() in "aeiou":
                    vowel = True
                else:
                    consonant = True
            elif not c.isdigit():
                return False

        return vowel and consonant