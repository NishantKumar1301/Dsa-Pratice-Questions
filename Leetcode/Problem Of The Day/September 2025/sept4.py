#Question : Find Closest Person
#Link to the question:  https://leetcode.com/problems/find-closest-person/
class Solution(object):
    def findClosest(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: int
        """
        diff_x = abs(x-z)
        diff_y = abs(y-z)
        if diff_x<diff_y:
            return 1
        elif diff_x==diff_y:
            return 0
        else:
            return 2
        