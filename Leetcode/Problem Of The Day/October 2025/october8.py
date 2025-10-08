#Question : Successful Pairs of Spells and Potions
#Link to the question: https://leetcode.com/problems/successful-pairs-of-spells-and-potions/ 
from bisect import bisect_left


class Solution(object):
    def successfulPairs(self, spells, potions, success):
        """
        :type spells: List[int]
        :type potions: List[int]
        :type success: int
        :rtype: List[int]
        """
        #Method1 : Brute Force (TLE)
        # ans = [0]*len(spells)
        # for i in range(len(spells)):
        #     cnt =0
        #     for j in range(len(potions)):
        #         if spells[i]*potions[j]>=success:
        #             cnt+=1
        #         ans[i]=cnt
        # return ans

        ans = []
        potions.sort()
        maxi = potions[-1]
        for spell in spells:
            mini = (success+spell-1)//spell
            if mini>maxi:
                ans.append(0)
                continue
            idx = bisect_left(potions,mini)
            ans.append(len(potions)-idx)
        return ans