#Question : Split Array by Prime Indices
#Link to the question: https://leetcode.com/contest/biweekly-contest-161/problems/split-array-by-prime-indices/
class Solution(object):
    def splitArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        is_prime = [False,False]+[True]*(n-2)
        for i in range(2,int(n**0.5)+1):
            if is_prime[i]:
                for j in range(i*i,n,i):
                    is_prime[j]=False

        a=b =0
        for idx,val in enumerate(nums):
            if is_prime[idx]:
                a+=val
            else:
                b+=val

        return abs(b-a)