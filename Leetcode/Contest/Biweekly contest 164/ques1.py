#Question : Find The Least Frequent Digit
#Link to the question: https://leetcode.com/contest/biweekly-contest-164/problems/find-the-least-frequent-digit/
class Solution(object):
    def getLeastFrequentDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        s = str(n)
        freq = {}
        for char in s:
            if char not in freq:
                freq[char]=1
            else:
                freq[char]+=1
        min_freq = min(freq.values())
        ans =  min(int(digit) for digit , cnt in freq.items() if cnt==min_freq)
        return ans