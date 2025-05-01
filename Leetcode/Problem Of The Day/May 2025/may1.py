#Question : Maximum Number of Tasks You Can Assign
#Link to the question: https://leetcode.com/problems/maximum-number-of-tasks-you-can-assign/description/?envType=daily-question&envId=2025-05-01

from sortedcontainers import SortedList
class Solution:
    def maxTaskAssign(self, tasks, workers, pills, strength):
        n, m = len(tasks), len(workers)
        tasks.sort()
        workers.sort()
        def check(mid):
            p = pills
            ws = SortedList(workers[m - mid :])
            for i in range(mid - 1, -1, -1):
                if ws[-1] >= tasks[i]:
                    ws.pop()
                else:
                    if p == 0:
                        return False
                    rep = ws.bisect_left(tasks[i] - strength)
                    if rep == len(ws):
                        return False
                    p -= 1
                    ws.pop(rep)
            return True
        left, right, ans = 1, min(m, n), 0
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        return ans