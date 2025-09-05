#Question : Minimum Operations to Make the Integer Zero
#Link to the question: https://leetcode.com/problems/minimum-operations-to-make-the-integer-zero/
class Solution(object):
    def makeTheIntegerZero(self, num1, num2):
        """
        :type num1: int
        :type num2: int
        :rtype: int
        """
        operations = 1

        while num1 - (operations * num2) >= operations:
            if bin(num1 - (operations * num2)).count('1') <= operations:
                return operations
            operations += 1

        return -1