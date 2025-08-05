#Question : Fruits Into Baskets II
#Link to the question: https://leetcode.com/problems/fruits-into-baskets-ii/
class Solution(object):
    def numOfUnplacedFruits(self, fruits, baskets):
        """
        :type fruits: List[int]
        :type baskets: List[int]
        :rtype: int
        """
        n = len(fruits)
        cnt = 0
        for fruit in fruits:
            for i in range(n):
                if baskets[i]>=fruit:
                    baskets[i]=float('-inf')
                    cnt+=1
                    break
        return n - cnt