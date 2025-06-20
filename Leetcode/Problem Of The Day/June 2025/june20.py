#Question : Maximum Manhattan Distance After K Changes
#Link to the question:  https://leetcode.com/problems/maximum-manhattan-distance-after-k-changes/

class Solution(object):
    def maxDistance(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        ans=north = south = east=west =0
        for i in range(len(s)):
            if s[i]=='N':north+=1
            if s[i]=='S':south+=1
            if s[i]=='E':east +=1
            if s[i]=='W':west+=1

            currdist = abs(north-south)+abs(east-west)
            step = i+1
            waste = step - currdist
            extra =0
            if waste!=0:
                extra = min(2*k,waste)
            finaldist = currdist+extra
            ans = max(ans,finaldist)
        return ans
        