#Question : Find Lucky Integer in an Array
#Link to the question:  https://leetcode.com/problems/find-lucky-integer-in-an-array/

from collections import Counter
class Solution(object):
    def findLucky(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        freq = Counter(arr)
        ans = -1
        for num, count in freq.items():
            if num == count:
                ans = max(ans, num)
        return ans
        