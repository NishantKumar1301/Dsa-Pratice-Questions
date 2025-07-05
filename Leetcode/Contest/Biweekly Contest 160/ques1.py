#Question : Hexadecimal and Hexatrigesimal Conversion
#Link to the question:  https://leetcode.com/contest/biweekly-contest-160/problems/hexadecimal-and-hexatrigesimal-conversion/

class Solution(object):
    def hexatrigesimal(self,n):
        ans = []
        d = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        if n == 0:
            return "0"
        while n > 0:
            ans.append(d[n%36])
            n = n//36
        return ''.join(reversed(ans))
        
    def concatHex36(self, n):
        """
        :type n: int
        :rtype: str
        """
        n2,n3 = n*n,n*n*n
        a = format(n2,'X')
        b = self.hexatrigesimal(n3)
        return a+b