#Question : Number of Equivalent Domino Pairs
#Link to the question: https://leetcode.com/problems/number-of-equivalent-domino-pairs/description/?envType=daily-question&envId=2025-05-04

class Solution(object):
    def numEquivDominoPairs(self, dominoes):
        """
        :type dominoes: List[List[int]]
        :rtype: int
        """
        num = [0] * 100
        ans = 0
        for x, y in dominoes:
            val = x * 10 + y if x <= y else y * 10 + x
            ans += num[val]
            num[val] += 1
        return ans
        