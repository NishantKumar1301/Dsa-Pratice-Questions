#Question : Count Number of Bad Pairs
#Link to the question: https://leetcode.com/problems/count-number-of-bad-pairs/description/?envType=daily-question&envId=2025-02-09


from collections import defaultdict
class Solution(object):
    def countBadPairs(self, nums):
        """
        :type nums: List[int]
        :r type: int
        """
        freq = defaultdict(int)
        n = len(nums)
        good_pair =0
        for i in range(n):
            key = nums[i]-i
            if key in freq:
                good_pair+=freq[key]
            freq[key]+=1
        total_pair = (n*(n-1))//2
        bad_pair = total_pair - good_pair
        return bad_pair