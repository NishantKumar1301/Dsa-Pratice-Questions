#Question : Painting a Grid With Three Different Colors
#Link to the question: https://leetcode.com/problems/painting-a-grid-with-three-different-colors/description/?envType=daily-question&envId=2025-05-18

from collections import defaultdict

class Solution(object):
    def colorTheGrid(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        MOD = 10**9 + 7
        valid = dict()
        for mask in range(3**m):
            color = []
            mm = mask
            for _ in range(m):
                color.append(mm % 3)
                mm //= 3
            if any(color[i] == color[i + 1] for i in range(m - 1)):
                continue
            valid[mask] = color
        adj = defaultdict(list)
        for mask1, color1 in valid.items():
            for mask2, color2 in valid.items():
                if not any(x == y for x, y in zip(color1, color2)):
                    adj[mask1].append(mask2)
        f = [int(mask in valid) for mask in range(3**m)]
        for _ in range(1, n):
            g = [0] * (3**m)
            for mask2 in valid:
                for mask1 in adj[mask2]:
                    g[mask2] += f[mask1]
                    if g[mask2] >= MOD:
                        g[mask2] -= MOD
            f = g
        return sum(f) % MOD


