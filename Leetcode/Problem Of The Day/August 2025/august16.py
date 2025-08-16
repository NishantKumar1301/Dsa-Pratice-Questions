#Question : Maximum 69 Number
#Link to the question: https://leetcode.com/problems/maximum-69-number/

class Solution(object):
    def maximum69Number (self, num):
        """
        :type num: int
        :rtype: int
        """
        num = list(str(num))
        n = len(num)
        for i in range(n):
            if num[i]=='6':
                num[i]='9'
                break
        return int("".join(num))