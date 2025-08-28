#Question : Minimum Window Substring
#Link to the question: https://leetcode.com/problems/minimum-window-substring/
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        left = right = 0
        sindex = -1
        cnt = 0
        minlen= float('inf')
        n = len(s)
        mp ={}
        for char in t:
            if char in mp :
                mp[char]+=1
            else:
                mp[char]=1
        
        while right < n:
            char = s[right]
            if char in mp and mp[char] > 0:
                cnt += 1
            if char in mp:
                mp[char]-=1
            else:
                mp[char]=-1
            
            while cnt == len(t):
                if right - left + 1 < minlen:
                    minlen = right - left + 1
                    sindex = left
                
                if s[left] in mp:
                    mp[s[left]]+=1
                else:
                    mp[s[left]]=1
                
                if mp[s[left]] > 0:
                    cnt -= 1
                left += 1
            
            right += 1
        
        return "" if sindex == -1 else s[sindex:sindex + minlen]