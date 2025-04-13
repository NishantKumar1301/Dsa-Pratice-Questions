#Question : Smallest Palindromic Rearrangement I
#Link to the question: https://leetcode.com/contest/weekly-contest-445/problems/smallest-palindromic-rearrangement-i/description/?slug=find-closest-person&region=global_v2

class Solution(object):
    def smallestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        freq= [0]*26
        for i in range(n):
            freq[ord(s[i])- ord('a')]+=1
        l = []
        m = ""
        for i in range(len(freq)):
            l.extend([chr(i + ord('a'))] * (freq[i] // 2))
            if freq[i]%2==1:
                m= chr(i+ord('a'))
        r= l[::-1]
        return ''.join(l) + m + ''.join(r)
        

