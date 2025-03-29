#Question : Apply Operations to Maximize Score
#Link to the question: https://leetcode.com/problems/apply-operations-to-maximize-score/description/?envType=daily-question&envId=2025-03-29

from collections import deque


class Solution:
    MOD = int(1e9 + 7)

    def maximumScore(self, nums, k):
        n = len(nums)
        ps = [0] * n
        max_num = max(nums)
        primes = self.get_primes(max_num)

        for i in range(n):
            num = nums[i]
            for p in primes:
                if p * p > num:
                    break
                if num % p != 0:
                    continue
                ps[i] += 1
                while num % p == 0:
                    num //= p
            if num > 1:
                ps[i] += 1

        next_d = [n] * n
        prev_d = [-1] * n
        stack = deque()

        for i in range(n):
            while stack and ps[stack[-1]] < ps[i]:
                idx = stack.pop()
                next_d[idx] = i
            if stack:
                prev_d[i] = stack[-1]
            stack.append(i)

        subarrays = [(next_d[i] - i) * (i - prev_d[i]) for i in range(n)]
        sorted_arr = sorted(enumerate(nums), key=lambda x: -x[1])

        score = 1

        def _power(base, exp):
            res = 1
            while exp > 0:
                if exp % 2:
                    res = (res * base) % self.MOD
                base = (base * base) % self.MOD
                exp //= 2
            return res

        idx = 0
        while k > 0:
            i, num = sorted_arr[idx]
            idx += 1
            ops = min(k, subarrays[i])
            score = (score * _power(num, ops)) % self.MOD
            k -= ops

        return score

    def get_primes(self, limit) :
        is_prime = [True] * (limit + 1)
        primes = []
        for num in range(2, limit + 1):
            if not is_prime[num]:
                continue
            primes.append(num)
            for m in range(num * num, limit + 1, num):
                is_prime[m] = False
        return primes


