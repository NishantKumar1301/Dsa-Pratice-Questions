#Question : Check if Any Element Has Prime Frequency
#Link to the question:  https://leetcode.com/contest/weekly-contest-455/problems/check-if-any-element-has-prime-frequency/

class Solution(object):
    def isPrime(self,n):
        if n<=1:
            return False
        if n==2 or n ==3:
            return True
        for i in range(2,n):
            if n%i==0:
                return False
        return True
    def checkPrimeFrequency(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        freq ={}
        for num in nums:
            if num in freq:
                freq[num]+=1
            else:
                freq[num]=1
        for num , count in freq.items():
            if self.isPrime(count):
                return True
        return False