#Question : Fruit Into Baskets
#Link to the question: https://leetcode.com/problems/fruit-into-baskets/

from collections import defaultdict
class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        freq = defaultdict(int)
        n = len(fruits)
        i=j=ans = 0
        while j<n:
            freq[fruits[j]]+=1
            if len(freq)<=2:
                ans = max(ans,j-i+1)
            else:
                freq[fruits[i]]-=1
                if freq[fruits[i]]==0:
                    del freq[fruits[i]]
                i+=1
            j+=1
        return ans
        