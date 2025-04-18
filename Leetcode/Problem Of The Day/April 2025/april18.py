#Question : Count and Say
#Link to the question : https://leetcode.com/problems/count-and-say/description/?envType=daily-question&envId=2025-04-18

class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        ans = ""
        if n==1:
            return "1"
        i=0
        s = self.countAndSay(n-1)
        while i<len(s):
            char = s[i]
            cnt = 1
            while i < len(s)-1 and s[i]==s[i+1]:
                cnt+=1
                i+=1
            ans += str(cnt)+char
            i+=1
        return ans


