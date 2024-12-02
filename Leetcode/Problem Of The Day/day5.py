#Question : Check If a Word Occurs As a Prefix of Any Word in a Sentence
#Link to the question: https://leetcode.com/problems/check-if-a-word-occurs-as-a-prefix-of-any-word-in-a-sentence/description/?envType=daily-question&envId=2024-12-02


class Solution(object):
    def isPrefixOfWord(self, sentence, searchWord):
        """
        :type sentence: str
        :type searchWord: str
        :rtype: int
        """
        words = sentence.split(" ")
        
        for i, word in enumerate(words):
            if word.startswith(searchWord):
                return i + 1  
        
        return -1


        

