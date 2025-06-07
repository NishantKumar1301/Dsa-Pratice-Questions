#Question : Maximize Y‑Sum by Picking a Triplet of Distinct X‑Values
#Link to the question:https://leetcode.com/contest/biweekly-contest-158/problems/maximize-ysum-by-picking-a-triplet-of-distinct-xvalues/
class Solution(object):
    def maxSumDistinctTriplet(self, x, y):
        """
        :type x: List[int]
        :type y: List[int]
        :rtype: int
        """
        freq ={}
        for i,j in zip(x,y):
            if i not in freq or j > freq[i]:
                freq[i]=j
        ans = sorted(freq.values(),reverse=True)
        if len(freq)<3:
            return -1
        return sum(ans[:3])