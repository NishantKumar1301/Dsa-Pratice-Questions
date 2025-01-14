#Question : Find the Prefix Common Array of Two Arrays
#Link to the question: https://leetcode.com/problems/find-the-prefix-common-array-of-two-arrays/description/


class Solution(object):
    def findThePrefixCommonArray(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        n = len(A)
        prefix_common_array = [0 for _ in range(n)]
        frequency = [0 for _ in range(n + 1)]
        common_count = 0

        for current_index in range(n):

            frequency[A[current_index]] += 1
            if frequency[A[current_index]] == 2:
                common_count += 1

            frequency[B[current_index]] += 1
            if frequency[B[current_index]] == 2:
                common_count += 1

            prefix_common_array[current_index] = common_count

        return prefix_common_array
        