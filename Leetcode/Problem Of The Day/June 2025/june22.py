#Question : Divide a String Into Groups of Size k
#Link to the question:  https://leetcode.com/problems/divide-a-string-into-groups-of-size-k/

class Solution(object):
    def divideString(self, s, k, fill):
        """
        :type s: str
        :type k: int
        :type fill: str
        :rtype: List[str]
        """
        ans =[]
        n = len(s)
        for i in range(0,n,k):
            j = n-1 if i+k-1>=n else i+k-1
            tmp = s[i:j+1]
            if len(tmp)<k:
                rem = k-len(tmp)
                tmp +=rem*fill
            ans.append(tmp)
        return ans