#Question : Number of Substrings Containing All Three Characters
#Link to the question: https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/
class Solution:
    def numberOfSubstrings(self, s):
        #create a freq array to store the frequency of a,b,c
        freq=[-1,-1,-1]
        cnt = 0
        for i in range(len(s)):
            freq[ord(s[i])-ord('a')]=i
            if freq[0]!=-1 and freq[1]!=-1 and freq[2]!=-1:
                cnt+=1+min(freq[0],freq[1],freq[2])
        return cnt
