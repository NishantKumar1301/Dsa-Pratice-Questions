#Question : Minimum Jumps to Reach End via Prime Teleportation
#Link to the question: https://leetcode.com/contest/weekly-contest-460/problems/minimum-jumps-to-reach-end-via-prime-teleportation/
class Solution(object):
    def minJumps(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        n , freq= len(nums), defaultdict(list)
        MAXI = max(nums) if nums else 2
        is_prime = [False, False] + [True] * (MAXI - 1)
        for i in range(2, int(MAXI ** 0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, MAXI + 1, i):
                    is_prime[j] = False
        for i, val in enumerate(nums):
            if i < 2:
                continue
            v, p = val, 2
            while p * p <= v:
                if v % p == 0:
                    if is_prime[p]:
                        freq[p].append(i)
                    while v % p == 0:
                        v //= p
                p += 1
            if v > 1 and is_prime[v]:
                freq[v].append(i)

        queue, visited = deque([(0, 0)]), [False] * n
        visited[0] = True

        while queue:
            idx, dis = queue.popleft()
            if idx == n - 1:
                return dis
            for ni in (idx - 1, idx + 1):
                if 0 <= ni < n and not visited[ni]:
                    visited[ni] = True
                    queue.append((ni, dis + 1))
            val = nums[idx]
            if val >= 2 and is_prime[val] and val in freq:
                for j in freq[val]:
                    if not visited[j]:
                        visited[j] = True
                        queue.append((j, dis + 1))
                freq.pop(val)

        return -1