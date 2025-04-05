#Question : Sum of All Subset XOR Totals
#Link to the question: https://leetcode.com/problems/sum-of-all-subset-xor-totals/description/


class Solution:
    def subsetXORSum(self, nums):

        def helper(nums, index, subset, subsets):
            if index == len(nums):
                subsets.append(subset[:])
                return

            subset.append(nums[index])
            helper(nums, index + 1, subset, subsets)
            subset.pop()

            helper(nums, index + 1, subset, subsets)

        subsets = []
        helper(nums, 0, [], subsets)

        ans = 0
        for subset in subsets:
            subset_XOR_total = 0
            for num in subset:
                subset_XOR_total ^= num
            ans += subset_XOR_total

        return ans