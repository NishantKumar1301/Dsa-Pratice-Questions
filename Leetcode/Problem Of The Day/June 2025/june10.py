#Question : Maximum Difference Between Even and Odd Frequency I
#Link to the question: https://leetcode.com/problems/maximum-difference-between-even-and-odd-frequency-i/
from collections import Counter
class Solution(object):
    def maxDifference(self, s):
        """
        :type s: str
        :rtype: int
        """
        #a= max(odd_freq_char), b = min(even_freq_char)
        freq= Counter(s)
        a= float('-inf')
        b = float('inf')
        for val in freq.values():
            if val%2==1:
                a = max(val,a)
            else:
                b = min(b,val)
        return a-b
