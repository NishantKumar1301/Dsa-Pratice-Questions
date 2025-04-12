#Question : Number of Unique XOR Triplets I
#Link to the question: https://leetcode.com/contest/biweekly-contest-154/problems/number-of-unique-xor-triplets-i/description/?slug=minimum-operations-to-make-array-sum-divisible-by-k&region=global_v2

class Solution(object):
    def uniqueXorTriplets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # s = set()
        # n = len(nums)
        # for i in range(n):
        #     for j in range(n):
        #         for k in range(n):
        #             val = nums[i]^(nums[j]^nums[k])
        #             s.add(val)
        # return len(s)

        n = len(nums)
        ans = 0
        if n<3:
            return n
        while 1<<ans<n+1:
            ans+=1
        return 1<<ans


