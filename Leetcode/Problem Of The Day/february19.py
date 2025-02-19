#Question : The k-th Lexicographical String of All Happy Strings of Length n
#Link to the question: https://leetcode.com/problems/the-k-th-lexicographical-string-of-all-happy-strings-of-length-n/description/?envType=daily-question&envId=2025-02-19

from collections import deque

class Solution:
    def getHappyString(self, n, k) :
        arr = []
        q = deque()

        q.append("a")
        q.append("b")
        q.append("c")

        while q:
            curr = q.popleft()
            if len(curr) == n:
                arr.append(curr)
                continue

            last = curr[-1]
            if last == 'a':
                q.append(curr + 'b')
                q.append(curr + 'c')
            elif last == 'b':
                q.append(curr + 'a')
                q.append(curr + 'c')
            else:
                q.append(curr + 'a')
                q.append(curr + 'b')

        if len(arr) < k:
            return ""
        return arr[k - 1]