#Question : K-th Smallest in Lexicographical Order
#Link to the question:https://leetcode.com/problems/k-th-smallest-in-lexicographical-order/description/
class Solution(object):
    def countNumber(self, curr, nxt, n):
        cnt = 0
        while curr <= n:
            cnt += min(n + 1, nxt) - curr
            curr *= 10
            nxt *= 10
        return cnt

    def findKthNumber(self, n, k):
        ans = 1
        k -= 1
        while k > 0:
            cnt = self.countNumber(ans, ans + 1, n)
            if k >= cnt:
                ans += 1
                k -= cnt
            else:
                ans *= 10
                k -= 1
        return ans
