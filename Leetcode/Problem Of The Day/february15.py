#Question : Find the Punishment Number of an Integer
#Link to the question: https://leetcode.com/problems/find-the-punishment-number-of-an-integer/description/?envType=daily-question&envId=2025-02-15


class Solution(object):
    def check(self, num, currnum, target):
        if num == 0:
            return currnum == target
        
        str_num = str(num)
        for i in range(1, len(str_num) + 1):
            if self.check(int(str_num[i:]) if i < len(str_num) else 0, currnum + int(str_num[:i]), target):
                return True
        return False

    def punishmentNumber(self, n):
        """
        :type n: int
        :r type: int
        """
        punishment_num = 0
        for current_num in range(1, n + 1):
            square_num = current_num * current_num
            if self.check(square_num, 0, current_num):
                punishment_num += square_num
        return punishment_num
