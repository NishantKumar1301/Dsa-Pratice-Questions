#Question : String Matching in an Array
#Link to the question: https://leetcode.com/problems/string-matching-in-an-array/description/


class Solution(object):
    def stringMatching(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        ans = []

        for curr in range(len(words)):
            for other in range(len(words)):
                if curr == other:
                    continue
                if words[curr] in words[other]:
                    ans.append(words[curr])
                    break  
        return ans
        