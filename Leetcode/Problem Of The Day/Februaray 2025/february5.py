#Question : Check if One String Swap Can Make Strings Equal
#Link to the question: https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal/description/?envType=daily-question&envId=2025-02-05

class Solution(object):
    def areAlmostEqual(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        count = 0
        s=[]
        n = len(s1)
        if s1==s2:
            return True
        for i in range(n):
            if s1[i]!=s2[i]:
                count+=1
                if count>2:
                    return False
                s.append(s1[i])
                s.append(s2[i])
                
        if count==2 and (s[0]==s[3] and s[1]==s[2]):
            return True
        else:
            return False
        

