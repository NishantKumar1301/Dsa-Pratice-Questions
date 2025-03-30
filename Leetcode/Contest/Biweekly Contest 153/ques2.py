#Question : Maximize Active Section with Trade I
#Link to the question: https://leetcode.com/problems/maximize-active-section-with-trade-i/description/


class Solution(object):
    def maxActiveSectionsAfterTrade(self, s):
        """
        :type s: str
        :r type: int
        """
        n = len(s)
        one = s.count('1')
        s = '1' + s + '1'
        m = n+2
        ans = one
        
        start = 1
        while start < m - 1:
            if s[start] == '1':
                j = start
                while j < m and s[j] == '1':
                    j += 1
                if j < m - 1 and s[start- 1] == '0' and s[j] == '0':
                    a, c = 0, 0
                    k = start - 1
                    while k >= 0 and s[k] == '0':
                        a += 1
                        k -= 1
                    k = j
                    while k < m and s[k] == '0':
                        c += 1
                        k += 1
                    ans = max(ans, one + a + c)
                start = j
            else:
                start += 1
        return ans
