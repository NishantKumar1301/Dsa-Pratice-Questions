#Question : Number of Unique XOR Triplets II
#Link to the question: https://leetcode.com/contest/biweekly-contest-154/problems/number-of-unique-xor-triplets-ii/description/?slug=number-of-unique-xor-triplets-i&region=global_v2

class Solution(object):
    def uniqueXorTriplets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # n = len(nums)
        # s= set()
        # for i in range(n):
        #     xor_sum =0
        #     for j in range(i,n):
        #         for k in range(n):
        #             # val = nums[i]^(nums[j]^nums[k])
        #             xor_sum = xor_sum^nums[j]
        #             s.add(xor_sum)
        # return len(s)
        # n = len(nums)
        # cnt = 0
        # if n <3:
        #     return n
        # while 1<<cnt<n+1:
        #     cnt+=1
        # return 1<<cnt

        # n = len(nums)
        # s = set()
        # for i in range(n):
        #     for j in range(i, n):
        #         s.add(nums[i] ^ nums[j])
        # s1 = set()
        # for num in s:
        #     for k in range(n):
        #         s1.add(num ^ nums[k])
        # return len(s1)
        
        arr = list(set(nums))
        dp = [set() for _ in range(4)]
        dp[0].add(0)

        for num in arr:
            for k in range(3, 0, -1):
                for val in dp[k - 1]:
                    dp[k].add(val ^ num)

        ans = set(nums)
        ans.update(dp[3])
        return len(ans)        














