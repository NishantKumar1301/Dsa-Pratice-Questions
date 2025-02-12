#Question : Max Sum of a Pair With Equal Sum of Digits
#Link to the question: https://leetcode.com/problems/max-sum-of-a-pair-with-equal-sum-of-digits/description/?envType=daily-question&envId=2025-02-12


from collections import defaultdict
class Solution(object):
    def calculate_digit_sum(self,n):
        sum_=0
        while n :
            sum_+=n%10
            n = n//10
        return sum_
    def maximumSum(self, nums):
        freq = defaultdict(int)
        ans =-1
        for num in nums:
            digit_sum = self.calculate_digit_sum(num)
            if digit_sum in freq:
                ans = max(ans,ans+freq[digit_sum])
                freq[digit_sum]=max(digit_sum,freq[digit_sum])
            else:
                freq[digit_sum]=nums
        return ans
