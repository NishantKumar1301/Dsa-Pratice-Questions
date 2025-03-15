#Question :  Unique 3-Digit Even Numbers
#Link to the question: https://leetcode.com/contest/biweekly-contest-152/problems/unique-3-digit-even-numbers/description/

from itertools import permutations
class Solution(object):
    def totalNumbers(self, digits):
        """
        :type digits: List[int]
        :rtype: int
        """
        s = set()

        for perm in permutations(digits, 3):
            if perm[0] == 0:
                continue
            if perm[2] % 2 != 0:
                continue
            s.add(perm)
        
        return len(s)
        