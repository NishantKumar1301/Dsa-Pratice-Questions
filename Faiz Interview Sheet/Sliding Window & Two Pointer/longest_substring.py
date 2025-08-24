#Question : Longest Substring Without Repeating Characters
#Link to the question: https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        #The ascii value of the chacter can be in the range of 0-255
        #Create array of size 255 initially marked every character as -1 , denoting its absent and index =-1
        #While iterating update mp[s[idx]]=idx
        n = len(s)
        maxLen = 0
        left = right = 0
        mp = [-1]*256
        while right<n:
            if mp[ord(s[right])]!=-1:
                #Update the left pointer
                left = max(left,mp[ord(s[right])]+1)
            mp[ord(s[right])]=right
            win_length = right-left+1
            maxLen = max(maxLen,win_length)
            right+=1    
        return maxLen