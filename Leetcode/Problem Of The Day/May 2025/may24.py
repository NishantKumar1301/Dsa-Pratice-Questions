#Question : Longest Palindrome by Concatenating Two Letter Words
#Link to the question: https://leetcode.com/problems/longest-palindrome-by-concatenating-two-letter-words/?envType=daily-question&envId=2025-05-25

from collections import defaultdict
class Solution(object):
    def longestPalindrome(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        freq = defaultdict(int)
        ans = 0
        for word in words:
            reversed_word=word[::-1]
            if freq[reversed_word]>0:
                ans+=4
                freq[reversed_word]-=1
            else:
                freq[word]+=1

        # Check for one possible center word with equal characters
        for word,count in freq.items():
            if word[0]==word[1] and freq[word]>0:
                ans+=2
                break
        
        return ans
        