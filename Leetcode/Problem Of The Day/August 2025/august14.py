#Question : Largest 3-Same-Digit Number in String
#Link to the question: https://leetcode.com/problems/largest-3-same-digit-number-in-string/
class Solution(object):
    def largestGoodInteger(self, num):
        """
        :type num: str
        :rtype: str
        """
        arr = ['999' , '888' , '777' , '666' , '555', '444','333','222','111','000']
        ans  = ""
        for n in arr:
            if n in num:
                ans = n
                break
        return ans