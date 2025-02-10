#Question : Clear Digits
#Link to the question: https://leetcode.com/problems/clear-digits/description/

class Solution(object):
    def clearDigits(self, s):
        """
        :type s: str
        :r type: str
        """
        stack = []
        for char in s:
            if stack and char.isdigit():
                stack.pop()
            else:
                stack.append(char)
        return "".join(stack)
        

