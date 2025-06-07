#Question :Lexicographically Minimum String After Removing Stars
#Link to the question: https://leetcode.com/problems/lexicographically-minimum-string-after-removing-stars/description/
class Solution(object):
    def clearStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        cnt = [[] for _ in range(26)]
        arr = list(s)
        for i, c in enumerate(arr):
            if c != "*":
                cnt[ord(c) - ord("a")].append(i)
            else:
                for j in range(26):
                    if cnt[j]:
                        arr[cnt[j].pop()] = "*"
                        break
        return "".join(c for c in arr if c != "*")
        