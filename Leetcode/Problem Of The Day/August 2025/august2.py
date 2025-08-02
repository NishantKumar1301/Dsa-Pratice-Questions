#Question : Rearranging Fruits
#Link to the question: https://leetcode.com/problems/rearranging-fruits
from collections import defaultdict

class Solution(object):
    def minCost(self, basket1, basket2):
        """
        :type basket1: List[int]
        :type basket2: List[int]
        :rtype: int
        """
        freq = defaultdict(int)
        mini = float('inf')

        for num in basket1:
            freq[num] += 1
            mini = min(mini, num)

        for num in basket2:
            freq[num] -= 1
            mini = min(mini, num)

        arr = []
        for cost, cnt in freq.items():
            if cnt == 0:
                continue
            if cnt % 2 != 0:
                return -1
            arr.extend([cost] * (abs(cnt) // 2))  

        if not arr:
            return 0

        arr.sort()
        ans = 0
        n = len(arr)
        for i in range(n // 2):
            ans += min(arr[i], mini * 2)

        return ans
