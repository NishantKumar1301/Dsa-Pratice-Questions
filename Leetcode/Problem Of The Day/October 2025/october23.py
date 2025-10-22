#Question : Maximum Frequency of an Element After Performing Operations II
#Link to the question: https://leetcode.com/problems/maximum-frequency-of-an-element-after-performing-operations-ii/
from bisect import bisect_left, bisect_right
from collections import Counter


class Solution(object):
    def maxFrequency(self, a, k, op):
        """
        :type nums: List[int]
        :type k: int
        :type numOperations: int
        :rtype: int
        """
        a,z = sorted(a),Counter(a)
        return max(max(min(bisect_right(a,v+k)-bisect_left(a,v-k)-z[v],op)+z[v],
            min(bisect_right(a,v+2*k)-i,op)) for i,v in enumerate(a))