#Question : Count of Substrings Containing Every Vowel and K Consonants II
#Link to the question: https://leetcode.com/problems/count-of-substrings-containing-every-vowel-and-k-consonants-ii/description/?envType=daily-question&envId=2025-03-10

class Solution:
    def _isVowel(self, c):
        return c == "a" or c == "e" or c == "i" or c == "o" or c == "u"

    def countOfSubstrings(self, word, k) :
        ans = 0
        start = end = 0
        freq = {} 
        cnt1 = 0  
        next_consonant = [0] * len(
            word
        )  
        next_consonant_index = len(word)

        for i in range(len(word) - 1, -1, -1):
            next_consonant[i] = next_consonant_index
            if not self._isVowel(word[i]):
                next_consonant_index = i

        while end < len(word):
            new_letter = word[end]
            if self._isVowel(new_letter):
                freq[new_letter] = freq.get(new_letter, 0) + 1
            else:
                cnt1 += 1

            while (
                cnt1 > k
            ): 
                start_letter = word[start]
                if self._isVowel(start_letter):
                    freq[start_letter] -= 1
                    if freq[start_letter] == 0:
                        del freq[start_letter]
                else:
                    cnt1 -= 1
                start += 1

            while (
                start < len(word)
                and len(freq) == 5
                and cnt1 == k
            ): 
                ans += next_consonant[end] - end
                start_letter = word[start]
                if self._isVowel(start_letter):
                    freq[start_letter] -= 1
                    if freq[start_letter] == 0:
                        del freq[start_letter]
                else:
                    cnt1 -= 1
                start += 1

            end += 1

        return ans