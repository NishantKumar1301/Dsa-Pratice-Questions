#Question :Construct K Palindrome Strings
#Link to the question: https://leetcode.com/problems/construct-k-palindrome-strings/description/


class Solution(object):
    def canConstruct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: bool
        """
        if len(s) < k:
            return False
        if len(s) == k:
            return True
        freq = [0] * 26
        odd_count = 0

        for char in s:
            freq[ord(char) - ord("a")] += 1
        for count in freq:
            if count % 2 == 1:
                odd_count += 1
        return odd_count <= k
        