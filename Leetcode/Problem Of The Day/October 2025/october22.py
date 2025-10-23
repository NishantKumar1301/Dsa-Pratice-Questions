#Question : Check If Digits Are Equal in String After Operations I
#Link to the question: https://leetcode.com/problems/check-if-digits-are-equal-in-string-after-operations-i/
class Solution(object):
    def hasSameDigits(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n = len(s)
        s_list = list(s)
        for i in range(1, n - 1):
            for j in range(n - i):
                digit1 = ord(s_list[j]) - ord("0")
                digit2 = ord(s_list[j + 1]) - ord("0")
                s_list[j] = chr(((digit1 + digit2) % 10) + ord("0"))
        return s_list[0] == s_list[1]