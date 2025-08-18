#Question : 24 Game
#Link to the question: https://leetcode.com/problems/24-game/

from itertools import permutations

class Solution:
    def judgePoint24(self, cards):
        cards.sort()
        if self.isValid4(cards):
            return True
        for perm in permutations(cards):
            if self.isValid4(list(perm)):
                return True
        return False

    # Equivalent of isValid(vector<int>& cards)
    def isValid4(self, cards):
        a, b, c, d = cards
        if (self.isValid3(a+b, c, d) or self.isValid3(a-b, c, d) or
            self.isValid3(a*b, c, d) or (b != 0 and self.isValid3(a/b, c, d))):
            return True
        if (self.isValid3(a, b+c, d) or self.isValid3(a, b-c, d) or
            self.isValid3(a, b*c, d) or (c != 0 and self.isValid3(a, b/c, d))):
            return True
        if (self.isValid3(a, b, c+d) or self.isValid3(a, b, c-d) or
            self.isValid3(a, b, c*d) or (d != 0 and self.isValid3(a, b, c/d))):
            return True
        return False

    # Equivalent of isValid(double a,double b,double c)
    def isValid3(self, a, b, c):
        if (self.isValid2(a+b, c) or self.isValid2(a-b, c) or
            self.isValid2(a*b, c) or (b != 0 and self.isValid2(a/b, c))):
            return True
        if (self.isValid2(a, b+c) or self.isValid2(a, b-c) or
            self.isValid2(a, b*c) or (c != 0 and self.isValid2(a, b/c))):
            return True
        return False

    # Equivalent of isValid(double a,double b)
    def isValid2(self, a, b):
        return (abs(a+b-24) <= 1e-5 or abs(a-b-24) <= 1e-5 or
                abs(a*b-24) <= 1e-5 or (b != 0 and abs(a/b-24) <= 1e-5))
