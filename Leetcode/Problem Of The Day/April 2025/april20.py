#Question : Rabbits in Forest
#Link to the question: https://leetcode.com/problems/rabbits-in-forest/description/?envType=daily-question&envId=2025-04-20

class Solution(object):
    def numRabbits(self, answers):
        """
        :type answers: List[int]
        :rtype: int
        """
        mp = {}
        for x in answers:
            mp[x] = mp.get(x, 0) + 1
        ans = 0
        for x, cnt in mp.items():
            size = x + 1
            g = (cnt + size - 1) // size
            ans += g * size
        return ans

