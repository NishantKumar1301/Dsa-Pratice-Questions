#Question : Find the Lexicographically Largest String From the Box I
#Link to the question: https://leetcode.com/problems/find-the-lexicographically-largest-string-from-the-box-i/?envType=daily-question&envId=2025-06-04
class Solution(object):
    def answerString(self, word, numFriends):
        """
        :type word: str
        :type numFriends: int
        :rtype: str
        """
        if numFriends==1:
            return word
        n = len(word)
        longest = n-(numFriends-1)
        ans = ""
        for i in range(n):
            can_take = min(longest,n-i)
            ans = max(ans, word[i:i+can_take])
        return ans
        