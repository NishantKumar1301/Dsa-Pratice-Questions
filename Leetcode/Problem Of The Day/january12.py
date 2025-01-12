#Question : Check if a Parentheses String Can Be Valid
#Link to the question: https://leetcode.com/problems/check-if-a-parentheses-string-can-be-valid/description/?envType=daily-question&envId=2025-01-12

class Solution(object):
    def canBeValid(self, s, locked):
        """
        :type s: str
        :type locked: str
        :rtype: bool
        """
        length = len(s)

        if length % 2 == 1:
            return False

        open_brackets = []
        unlocked = []

        for i in range(length):
            if locked[i] == "0":
                unlocked.append(i)
            elif s[i] == "(":
                open_brackets.append(i)
            elif s[i] == ")":
                if open_brackets:
                    open_brackets.pop()
                elif unlocked:
                    unlocked.pop()
                else:
                    return False

        while open_brackets and unlocked and open_brackets[-1] < unlocked[-1]:
            open_brackets.pop()
            unlocked.pop()

        if open_brackets:
            return False

        return True
        


