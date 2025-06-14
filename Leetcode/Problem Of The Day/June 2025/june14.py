#Question : Maximum Difference by Remapping a Digit
#Link to the question: https://leetcode.com/problems/maximum-difference-by-remapping-a-digit/
class Solution(object):
    def minMaxDifference(self, num):
        """
        :type num: int
        :rtype: int
        """
        mini = str(num)
        maxi= str(num)
        n = len(mini)
        char = ''
        for i in range(n):
            if mini[i]!='9':
                char = mini[i]
                break
        if char:
            maxi = maxi.replace(char,'9')
        char0 = mini[0]
        mini =mini.replace(char0,'0')
        return int(maxi) - int(mini)