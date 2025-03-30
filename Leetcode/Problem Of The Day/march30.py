#Question : Partition Labels
#Link to the question: https://leetcode.com/problems/partition-labels/description/?envType=daily-question&envId=2025-03-30


class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        ans  = []
        last= [0]*26
        for i , char in enumerate(s):
            last[ord(char)-ord("a")]=i
        start=end=0
        for i , char in enumerate(s):
            end = max(end,last[ord(char)-ord("a")])
            if i==end:
                ans.append(i-start+1)
                start=i+1
        return ans