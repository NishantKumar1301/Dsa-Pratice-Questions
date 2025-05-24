#Question : Find Maximum Number of Non Intersecting Substrings
#Link to the question: https://leetcode.com/contest/biweekly-contest-157/problems/find-maximum-number-of-non-intersecting-substrings/?slug=sum-of-largest-prime-substrings&region=global_v2
from heapq import heappush,heappop
class Interval:
    def __init__(self, e, s, char, l, r):
        self.end = e
        self.start = s
        self.c = char
        self.left = l
        self.right = r

    def __lt__(self, other):
        return self.end < other.end

class Solution(object):
    def maxSubstrings(self, word):
        """
        :type word: str
        :rtype: int
        """
        ans,last = 0,-1
        freq = [[] for _ in range(26)]
        for i, char in enumerate(word):
            freq[ord(char) - ord('a')].append(i)
        pq = []
        for char in range(26):
            v,l,r = freq[char],0,1
            while l + 1 < len(v):
                while r < len(v) and v[r] - v[l] < 3:
                    r += 1
                if r == len(v):
                    break
                heappush(pq, Interval(v[r], v[l], char, l, r))
                l += 1
        while pq:
            curr =heappop(pq)
            if curr.start > last:
                last = curr.end
                ans += 1
            v , l = freq[curr.c], curr.left + 1
            r = max(curr.right, l + 1)
            while l + 1 < len(v):
                while r < len(v) and v[r] - v[l] < 3:
                    r += 1
                if r == len(v):
                    break
                heappush(pq, Interval(v[r], v[l], curr.c, l, r))
                break
        return ans