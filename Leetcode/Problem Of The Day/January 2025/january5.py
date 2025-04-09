#Question : Shifting Letters II
#Link to the question: https://leetcode.com/problems/shifting-letters-ii/description/


class Solution(object):
    def shift(self, a, n):
        i = ord(a) - ord('a')
        i = (i + n) % 26
        if i < 0:
            i += 26
        return chr(ord('a') + i)

    def shiftingLetters(self, s, shifts):
        n = len(s)
        totShift = [0] * (n + 1)
        for shift in shifts:
            if shift[2] == 0:
                totShift[shift[0]] -= 1
                totShift[shift[1] + 1] += 1
            else:
                totShift[shift[0]] += 1
                totShift[shift[1] + 1] -= 1
        for i in range(1, len(totShift)):
            totShift[i] += totShift[i - 1]
        result = list(s)
        for i in range(n):
            result[i] = self.shift(s[i], totShift[i])
        return "".join(result)
