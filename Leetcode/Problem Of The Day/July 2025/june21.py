#Question : Delete Characters to Make Fancy String
#Link to the question: https://leetcode.com/problems/delete-characters-to-make-fancy-string/

class Solution(object):
    def makeFancyString(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans = prev = s[0]
        n , freq = len(s),1
        for i in range(1,n):
            if s[i]==prev:
                freq+=1
            else:
                prev = s[i]
                freq = 1
            
            if freq<3:
                ans+=s[i]
        
        return ans