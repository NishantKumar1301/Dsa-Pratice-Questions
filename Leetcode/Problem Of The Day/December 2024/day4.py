#Question : Check if Numbers Are Ascending in a Sentence
#Link to the question: https://leetcode.com/problems/check-if-numbers-are-ascending-in-a-sentence/description/

class Solution(object):
    def areNumbersAscending(self, s):
        """
        :type s: str
        :rtype: bool
        """
        words = s.split(" ")
        lst =[]
        for word in words:
            if word.isdigit():
                lst.append(int(word))
        
        for i in range(len(lst)-1):
            if lst[i+1]<=lst[i]:
                return False
        return True
        

