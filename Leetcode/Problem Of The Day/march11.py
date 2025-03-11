#Question : Number of Substrings Containing All Three Characters
#Link to the question: https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/description/?envType=daily-question&envId=2025-03-11


class Solution:
    def numberOfSubstrings(self, s):
        left = right = ans = 0
        freq = [0] * 3

        while right < len(s):
            freq[ord(s[right]) - ord("a")] += 1

            while self.helper(freq):
                ans += len(s) - right
                freq[ord(s[left]) - ord("a")] -= 1
                left += 1

            right += 1

        return ans

    def helper(self, freq) :
        return all(f > 0 for f in freq)

