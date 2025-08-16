#Question : Valid Parentheses
#Link to the question: https://leetcode.com/problems/valid-parentheses/

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        n = len(s)
        for i in range(n):
            if s[i]=='(' or s[i]=='{' or s[i]=='[':
                stack.append(s[i])
            else:
                if len(stack)==0:
                    return True
                char = stack.pop()
                if (s[i]==')' and char =='(') or (s[i]=='}' and char =='{') or (s[i]==']' and char=='['):
                    return True
        return False