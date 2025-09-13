#Question : Find Most Frequent Vowel and Consonant
#Link to the question: https://leetcode.com/problems/find-most-frequent-vowel-and-consonant/
from collections import Counter
class Solution(object):
    def maxFreqSum(self, s):
        """
        :type s: str
        :rtype: int
        """
        mp = Counter(s)
        v =c= 0
        vowel = set("aeiou")
        for char, cnt in mp.items():
            if char in vowel:
                v = max(v, cnt)
            else:
                c = max(c, cnt)
        return v + c