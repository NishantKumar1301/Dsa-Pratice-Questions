#Question : Counting Words With a Given Prefix
#Link to the question: https://leetcode.com/problems/counting-words-with-a-given-prefix/description/

class Solution(object):
    def prefixCount(self, words, pref):
        """
        :type words: List[str]
        :type pref: str
        :rtype: int
        """
        count = 0
        for word in words:
            count += self._has_prefix(word, pref)
        return count

    def _has_prefix(self, string, pref):
        """
        Helper function to check if a string has the given prefix.
        :type string: str
        :type pref: str
        :rtype: int
        """
        itr = 0
        while itr < len(string) and itr < len(pref):
            if string[itr] != pref[itr]:
                return 0
            itr += 1

        if itr != len(pref):
            return 0
        return 1



