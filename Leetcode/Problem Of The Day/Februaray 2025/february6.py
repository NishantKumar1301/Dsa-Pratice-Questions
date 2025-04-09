#Question : Tuple with Same Product
#Link to the question: https://leetcode.com/problems/tuple-with-same-product/description/?envType=daily-question&envId=2025-02-06

class Solution(object):
    def nc2(self,val):
        return (val*(val-1))//2

    def tupleSameProduct(self, nums):
        """
        :type nums: List[int]
        :r type: int
        """
        freq={}
        n = len(nums)
        for i in range(n-1):
            for j in range(i+1,n):
                prod = nums[i]*nums[j]
                freq[prod]=freq.get(prod,0)+1
        ans =0
        for val in freq.values():
            if val>1:
                ans+=8* self.nc2(val)
        return ans
        

