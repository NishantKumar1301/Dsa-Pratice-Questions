#Question : Minimum Deletions to Make String K-Special
#Link to the question: https://leetcode.com/problems/minimum-deletions-to-make-string-k-special 

from collections import Counter
class Solution(object):
    def minimumDeletions(self, word, k):
        """
        :type word: str
        :type k: int
        :rtype: int
        """
        freq = Counter(word)
        ans = float('inf')
        for a in freq.values():
            p=0
            for b in freq.values():
                if a>b:
                    p+=b
                elif b>a+k:
                    p+=b-(a+k)
            ans = min(ans,p)
        return ans

        