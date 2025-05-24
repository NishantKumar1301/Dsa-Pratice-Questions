#Question : Find Maximum Number of Non Intersecting Substrings
#Link to the question: https://leetcode.com/contest/biweekly-contest-157/problems/find-maximum-number-of-non-intersecting-substrings/?slug=sum-of-largest-prime-substrings&region=global_v2
from collections import defaultdict
import bisect

class Solution(object):
    def maxSubstrings(self, word):
        """
        :type word: str
        :rtype: int
        """
        n = len(word)
        freq = defaultdict(list)
        for i, char in enumerate(word):
            freq[char].append(i)

        arr = []
        for val in freq.values():
            s = len(val)
            for i in range(s):
                target = val[i] + 3  
                idx = bisect.bisect_left(val, target, i + 1)
                if idx < s:
                    arr.append((val[i], val[idx]))
        arr.sort(key=lambda x: x[1])
        ans, last = 0, -1
        for i, j in arr:
            if i > last:
                ans += 1
                last = j
        return ans
