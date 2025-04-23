#Question : Count Largest Group
#Link to the question: https://leetcode.com/problems/count-largest-group/description/?envType=daily-question&envId=2025-04-23

import collections


class Solution(object):
    def countLargestGroup(self, n):
        """
        :type n: int
        :rtype: int
        """
        freq = collections.Counter()
        for i in range(1, n + 1):
            key = sum([int(x) for x in str(i)])
            freq[key] += 1
        maxi = max(freq.values())
        ans = sum(1 for v in freq.values() if v == maxi)
        return ans
        


