#Question : Minimum Recolors to Get K Consecutive Black Blocks
#Link to the question: https://leetcode.com/problems/minimum-recolors-to-get-k-consecutive-black-blocks/description/?envType=daily-question&envId=2025-03-08


class Solution:
    def minimumRecolors(self, blocks, k):
        left = 0
        w = 0
        ans = float("inf")

        for right in range(len(blocks)):

            if blocks[right] == "W":
                w += 1

            if right - left + 1 == k:

                ans = min(ans, w)

                if blocks[left] == "W":
                    w -= 1

                left += 1

        return ans