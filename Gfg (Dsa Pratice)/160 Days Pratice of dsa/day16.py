#Question : Non Repeating Character
#Link to the question: https://www.geeksforgeeks.org/batch/gfg-160-problems/track/string-gfg-160/problem/non-repeating-character-1587115620

class Solution:
    # Function to find the first non-repeating character in a string.
    def nonRepeatingChar(self, s):
        char_count = {}

        for char in s:
            char_count[char] = char_count.get(char, 0) + 1

        for char in s:
            if char_count[char] == 1:
                return char

        return '$'

