#Question : Reverse Degree of a String
#Link to the question: https://leetcode.com/problems/reverse-degree-of-a-string/description/

class Solution(object):
    def reverseDegree(self, s):
        """
        :type s: str
        :r type: int
        """
        ans = 0
        for i, char in enumerate(s, 1):  
            r = 26 - (ord(char) - ord('a')) 
            ans += r * i
        return ans
        

