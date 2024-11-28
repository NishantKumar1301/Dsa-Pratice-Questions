#Question : Count Digits
#Link to the question: https://www.geeksforgeeks.org/problems/count-digits5716/1

class Solution:
    def evenlyDivides(self, n):
        count = 0 
        m = str(n)
        for i in m:
            d = int(i)
            if d!=0 and  n % d == 0:
                count += 1
        return count

