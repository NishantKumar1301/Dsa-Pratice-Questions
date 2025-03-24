#Question : Count Days Without Meetings
#Link to the question: https://leetcode.com/problems/count-days-without-meetings/?envType=daily-question&envId=2025-03-24

class Solution(object):
    def countDays(self, days, meetings):
        """
        :type days: int
        :type meetings: List[List[int]]
        :rtype: int
        """
        ans = 0
        curr_end =0
        meetings.sort()
        # print(meetings)
        for start , end in meetings:
            if start > curr_end +1 :
                ans += start - curr_end-1
            curr_end = max(curr_end, end)
        ans += days - curr_end
        return ans
        

