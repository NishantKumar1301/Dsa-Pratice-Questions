#Question : Design Spreadsheet
#Link to the question: https://leetcode.com/contest/biweekly-contest-152/problems/design-spreadsheet/description/

class Spreadsheet(object):

    def __init__(self, rows):
        """
        :type rows: int
        """
        self.rows = rows
        self.cols = 26  
        self.freq = {}  

    def setCell(self, cell, value):
        """
        :type cell: str
        :type value: int
        :rtype: None
        """
        self.freq[cell] = value

    def resetCell(self, cell):
        """
        :type cell: str
        :rtype: None
        """
        if cell in self.freq:
            del self.freq[cell]

    def getValue(self, formula):
        """
        :type formula: str
        :rtype: int
        """
        formula = formula[1:]

        arr = formula.split('+')
        ans = 0

        for p in arr:
            if p.isdigit(): 
                ans += int(p)
            else: 
                ans += self.freq.get(p, 0)

        return ans
        


# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)©leetcode

