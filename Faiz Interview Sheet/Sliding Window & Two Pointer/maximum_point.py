#Question : Maximum Points You Can Obtain from Cards
#Link to the question: https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/
class Solution(object):
    def maxScore(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        lsum = rsum = maxsum =0
        #Step 1 : Find the left sum till k index
        for i in range(k):
            lsum+=cardPoints[i]
        maxsum = lsum
        #step 2 : shrink the left side sum and increase the rightsum window
        rightInd = len(cardPoints)-1
        for i in range(k-1,-1,-1):
            lsum-=cardPoints[i]
            rsum +=cardPoints[rightInd]
            rightInd-=1
            maxsum = max(maxsum,lsum+rsum)
        return maxsum