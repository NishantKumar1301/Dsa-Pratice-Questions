#Question : Maximum Candies You Can Get from Boxes
#Link to the question: Maximum Candies You Can Get from Boxes
class Solution(object):
    def maxCandies(self, status, candies, keys, containedBoxes, initialBoxes):
        """
        :type status: List[int]
        :type candies: List[int]
        :type keys: List[List[int]]
        :type containedBoxes: List[List[int]]
        :type initialBoxes: List[int]
        :r type: int
        """
        seen = set()
        can_look = set()
        def dfs(box):
            if box in seen:
                return 0
            if status[box] == 0:
                can_look.add(box)
                return 0
            seen.add(box)
            total = candies[box]
            for next_box in containedBoxes[box]:
                total += dfs(next_box)
            for next_box in keys[box]:
                status[next_box] = 1
                if next_box in can_look:
                    total += dfs(next_box)
            return total
        return sum([dfs(box) for box in initialBoxes])
        