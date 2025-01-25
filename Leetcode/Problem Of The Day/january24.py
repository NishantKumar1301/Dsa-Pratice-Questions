#Question : Make Lexicographically Smallest Array by Swapping Elements
#Link to the question: https://leetcode.com/problems/make-lexicographically-smallest-array-by-swapping-elements/description/?envType=daily-question&envId=2025-01-25

from collections import defaultdict, deque
class Solution:
    def lexicographicallySmallestArray(self, nums, limit):
        n = len(nums)

        vec = sorted(nums)  # Sort the array

        group_num = 0
        num_to_group = {vec[0]: group_num}

        group_to_list = defaultdict(deque)
        group_to_list[group_num].append(vec[0])

        for i in range(1, n):
            if abs(vec[i] - vec[i - 1]) > limit:
                group_num += 1

            num_to_group[vec[i]] = group_num
            group_to_list[group_num].append(vec[i])

        result = []
        for num in nums:
            group = num_to_group[num]
            result.append(group_to_list[group].popleft())

        return result

