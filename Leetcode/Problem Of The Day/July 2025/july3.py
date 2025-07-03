#Question : Find the K-th Character in String Game I
#Link to the question:  https://leetcode.com/problems/find-the-k-th-character-in-string-game-i

class Solution(object):
    def kthCharacter(self, k):
        """
        :type k: int
        :rtype: str
        """
        ans = "a"
        while len(ans)<k:
            for char in ans:
                ch = 'a' if char=='z' else chr(ord(char)+1)
                ans+=ch

        return ans[k-1]
        