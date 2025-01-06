#Question : Minimum Number of Operations to Move All Balls to Each Box
#Link to the question: https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box/

class Solution(object):
    def minOperations(self, boxes):
        """
        :type boxes: str
        :rtype: List[int]
        """
        ans = [0] * len(boxes)
        for curr in range(len(boxes)):
            if boxes[curr] == "1":
                for new_position in range(len(boxes)):
                    ans[new_position] += abs(new_position - curr)
        return ans
        


