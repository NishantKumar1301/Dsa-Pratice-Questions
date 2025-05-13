#Question : Total Characters in String After Transformations I
#Link to the question: https://leetcode.com/problems/total-characters-in-string-after-transformations-i/description/?envType=daily-question&envId=2025-05-13
MOD = 10**9+7
class Solution(object):
    def lengthAfterTransformations(self, s, t):
        """
        :type s: str
        :type t: int
        :return Type: int
        """
        freq = [0]*26
        for char in s:
            freq[ord(char)-ord('a')]+=1
        for _ in range(t):
            temp = [0]*26
            temp[0]= freq[25]%MOD
            temp[1]= (freq[0]+freq[25])%MOD
            for i in range(2,26):
                temp[i]=(freq[i-1])%MOD
            freq=temp
        return sum(freq)%MOD
