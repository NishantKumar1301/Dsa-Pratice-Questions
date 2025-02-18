#Question : Construct Smallest Number From DI String
#Link to the question: https://leetcode.com/problems/construct-smallest-number-from-di-string/description/?envType=daily-question&envId=2025-02-18

class Solution:
    def smallestNumber(self, pattern):
        n = len(pattern)
        st = []
        res = []

        for i in range(1, n + 2):
            st.append(i)
            if i == n + 1 or pattern[i - 1] == 'I':
                while st:
                    res.append(str(st.pop()))

        return ''.join(res)

