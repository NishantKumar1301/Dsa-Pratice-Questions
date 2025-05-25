#Question : Resulting String After Adjacent Removals
#Link to the question: https://leetcode.com/contest/weekly-contest-451/problems/resulting-string-after-adjacent-removals/?slug=find-minimum-log-transportation-cost&region=global_v2

class Solution(object):
    def resultingString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        for char in s:
            if stack:
                x = abs(ord(char)-ord(stack[-1]))
                if x==1 or x==25:
                    stack.pop()
                    continue
            stack.append(char)
        return ''.join(stack)