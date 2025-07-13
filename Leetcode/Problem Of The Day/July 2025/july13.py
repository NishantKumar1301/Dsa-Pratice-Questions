#Question : Maximum Matching of Players With Trainers
#Link to the question: https://leetcode.com/problems/maximum-matching-of-players-with-trainers/

class Solution(object):
    def matchPlayersAndTrainers(self, players, trainers):
        """
        :type players: List[int]
        :type trainers: List[int]
        :rtype: int
        """
        players.sort()
        trainers.sort()
        m, n = len(players), len(trainers)
        i = j = count = 0

        while i < m and j < n:
            while j < n and players[i] > trainers[j]:
                j += 1
            if j < n:
                count += 1
            i += 1
            j += 1

        return count