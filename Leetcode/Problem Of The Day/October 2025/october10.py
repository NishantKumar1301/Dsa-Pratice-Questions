#Question : Taking Maximum Energy From the Mystic Dungeon
#Link to the question: https://leetcode.com/problems/taking-maximum-energy-from-the-mystic-dungeon/
class Solution(object):
    def maximumEnergy(self, energy, k):
        """
        :type energy: List[int]
        :type k: int
        :rtype: int
        """
        n = len(energy)
        ans = float('-inf')
        for i in range(n - k, n):
            total = 0
            j = i
            while j >= 0:
                total += energy[j]
                ans = max(ans, total)
                j -= k
        return ans