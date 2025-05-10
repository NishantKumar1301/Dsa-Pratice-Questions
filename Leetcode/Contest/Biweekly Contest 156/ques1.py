#Question : Find Most Frequent Vowel and Consonant
#Link to the question: https://leetcode.com/contest/biweekly-contest-156/problems/find-most-frequent-vowel-and-consonant/description/
from collections import Counter
class Solution(object):
    def maxFreqSum(self, s):
        """
        :type s: str
        :returnType: int
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