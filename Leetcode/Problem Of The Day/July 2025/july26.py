#Question : Maximize Subarrays After Removing One Conflicting Pair
#Link to the question: https://leetcode.com/problems/maximize-subarrays-after-removing-one-conflicting-pair
class Solution(object):
    def maxSubarrays(self, n, conflictingPairs):
        """
        :type n: int
        :type conflictingPairs: List[List[int]]
        :rtype: int
        """
        valid = 0
        conflictingPoints = [[] for _ in range(n + 1)]

        for p in conflictingPairs:
            a = min(p[0], p[1])
            b = max(p[0], p[1])
            conflictingPoints[b].append(a)

        maxConflict = 0
        secondMaxConflict = 0
        extra = [0] * (n + 1)

        for end in range(1, n + 1):
            for u in conflictingPoints[end]:
                if u >= maxConflict:
                    secondMaxConflict = maxConflict
                    maxConflict = u
                elif u > secondMaxConflict:
                    secondMaxConflict = u

            valid += end - maxConflict
            extra[maxConflict] += maxConflict - secondMaxConflict

        return valid + max(extra)