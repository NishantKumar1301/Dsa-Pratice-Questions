#Question : Final Value of Variable After Performing Operations
#Link to the question: https://leetcode.com/problems/final-value-of-variable-after-performing-operations
class Solution(object):
    def finalValueAfterOperations(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        cnt = 0
        for operation in operations:
            if operation[1]=='+':
                cnt+=1
            else:
                cnt-=1
        return cnt