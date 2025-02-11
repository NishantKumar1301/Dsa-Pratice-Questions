#Question : Remove All Occurrences of a Substring
#Link to the question: https://leetcode.com/problems/remove-all-occurrences-of-a-substring/description/?envType=daily-question&envId=2025-02-11


class Solution(object):
    def check(self,stack,part,n):
        temp =stack[:]
        for i in range(n-1,-1,-1):
            if not temp or temp[-1]!=part[i]:
                return False
            temp.pop()
        return True 

    def removeOccurrences(self, s, part):
        """
        :type s: str
        :type part: str
        :r type: str
        """
        n = len(part)
        stack =[]
        for char in s:
            stack.append(char)
            if len(stack)>=n and self.check(stack,part,n):
                for _ in range(n):
                    stack.pop()
        return "".join(stack)
