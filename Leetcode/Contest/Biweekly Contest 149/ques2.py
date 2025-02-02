#Question : Reschedule Meetings for Maximum Free Time I
#Link to the question: https://leetcode.com/problems/reschedule-meetings-for-maximum-free-time-i/description/?slug=find-valid-pair-of-adjacent-digits-in-string&region=global_v2

class Solution(object):
    def maxFreeTime(self, eventTime, k, startTime, endTime):
        """
        :type eventTime: int
        :type k: int
        :type startTime: List[int]
        :type endTime: List[int]
        :rtype: int
        """
        n = len(startTime)
        gaps = []

        gaps.append(startTime[0])

        for i in range(1, n):
            gaps.append(startTime[i] - endTime[i - 1])

        gaps.append(eventTime - endTime[n - 1])

        total = sum(gaps[:k + 1])
        ans = total

        for i in range(k + 1, len(gaps)):
            total += gaps[i] - gaps[i - (k + 1)]
            ans = max(ans, total)

        return ans


