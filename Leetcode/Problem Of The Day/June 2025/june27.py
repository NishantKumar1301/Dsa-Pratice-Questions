#Question : Longest Subsequence Repeated k Times
#Link to the question: https://leetcode.com/problems/longest-subsequence-repeated-k-times/

class Solution(object):
    def longestSubsequenceRepeatedK(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        ans = ""
        candidate = sorted([c for c, w in Counter(s).items() if w >= k], reverse=True)
        q = deque(candidate)
        while q:
            curr = q.popleft()
            if len(curr) > len(ans):
                ans = curr
            for ch in candidate:
                nxt = curr + ch
                it = iter(s)
                if all(ch in it for ch in nxt * k):
                    q.append(nxt)
        return ans