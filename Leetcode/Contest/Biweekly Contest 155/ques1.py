#Question : Find the Most Common Response
#Link to the question: https://leetcode.com/contest/biweekly-contest-155/problems/find-the-most-common-response/description/?slug=unit-conversion-i&region=global_v2

class Solution(object):
    def findCommonResponse(self, responses):
        """
        :type responses: List[List[str]]
        :rtype: str
        """
        mp = {}
        for i in responses:
            visited = set(i)
            for res in visited:
                mp[res] = mp.get(res, 0) + 1
        maxi = 0
        ans = ""
        for key, val in mp.items():
            if val > maxi or (val == maxi and key < ans):
                maxi = val
                ans = key
        return ans

