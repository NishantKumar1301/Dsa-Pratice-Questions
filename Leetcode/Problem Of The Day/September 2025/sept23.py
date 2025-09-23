#Question : Compare Version Numbers
#Link to the question: https://leetcode.com/problems/compare-version-numbers/
class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        vs1, vs2 = version1.split("."), version2.split(".")
        m, n = len(vs1), len(vs2)
        for i in range(max(m, n)):
            v1 = int(vs1[i]) if i < m else 0
            v2 = int(vs2[i]) if i < n else 0
            if v1 < v2:
                return -1
            if v1 > v2:
                return 1
        return 0