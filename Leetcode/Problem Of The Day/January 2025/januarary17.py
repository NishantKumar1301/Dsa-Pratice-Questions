#Question : Neighboring Bitwise XOR
#Link to the question: https://leetcode.com/problems/neighboring-bitwise-xor/description/


class Solution(object):
    def doesValidArrayExist(self, derived):
        """
        :type derived: List[int]
        :rtype: bool
        """
        ans = 0
        for num in derived:
            ans = ans^num
        if ans ==0:
            return True
        else:
            return False
        


