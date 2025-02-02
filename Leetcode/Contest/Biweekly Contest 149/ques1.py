#Question : Find Valid Pair of Adjacent Digits in String
#Link to the question: https://leetcode.com/problems/find-valid-pair-of-adjacent-digits-in-string/description/

class Solution(object):
    def findValidPair(self, s):
        n = len(s)
        freq = {}
        for char in s :
            if char in freq:
                freq[char]+=1
            else:
                freq[char]=1
        for i in range(n-1):
            if s[i]!=s[i+1]:
                if freq[s[i]]==int(s[i]) and freq[s[i+1]]==int(s[i+1]):
                    return s[i]+s[i+1]
        return ""
        

