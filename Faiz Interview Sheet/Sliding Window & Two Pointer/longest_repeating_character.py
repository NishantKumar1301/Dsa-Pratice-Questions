#Question : Longest Repeating Character Replacement
#Link to the question: https://leetcode.com/problems/longest-repeating-character-replacement/
class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        #Condition : length - maxFreq <=k then only update maxlen , length = right-left+1
        left = right = maxlen = maxfreq = 0
        freq = [0]*26
        n = len(s)
        while right<n:
            freq[ord(s[right])-ord('A')]+=1
            maxfreq = max(maxfreq,freq[ord(s[right])-ord('A')])
            #Shrink the window if length-maxFreq>k
            if (right-left+1)-maxfreq>k:
                freq[ord(s[left])-ord('A')]-=1
                left+=1
            #Else update maxlen
            else:
                maxlen = max(maxlen,right-left+1)
            right+=1
        return maxlen