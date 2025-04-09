#Question : Alternating Groups II
#Link to the question: https://leetcode.com/problems/alternating-groups-ii/description/?envType=daily-question&envId=2025-03-09


class Solution:
    def numberOfAlternatingGroups(self, colors, k):
        l = len(colors)
        ans = 0
        a = 1  
        last = colors[0]

        for i in range(1, l + k - 1):
            index = i % l  

            if colors[index] == last:
                a = 1
                last = colors[index]
                continue

            a += 1

            if a >= k:
                ans += 1

            last = colors[index]

        return ans