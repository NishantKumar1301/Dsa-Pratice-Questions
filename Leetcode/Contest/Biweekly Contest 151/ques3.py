#Question : Find Minimum Cost to Remove Array Elements
#Link to the question: https://leetcode.com/problems/find-minimum-cost-to-remove-array-elements/description/

class Solution(object):
    def __init__(self):
        self.dpMemo = []
        self.arr = []
        self.arrSize = 0
    
    def computeCost(self, index, anchor):
        if anchor in self.dpMemo[index]:
            return self.dpMemo[index][anchor]
        
        remaining = 1 + (self.arrSize - index)
        minCost = 0
        if remaining < 3:
            if remaining == 1:
                minCost = anchor
            else:
                minCost = max(anchor, self.arr[index])
        else:
            first = anchor
            second = self.arr[index]
            third = self.arr[index + 1]
            caseA = max(second, third) + self.computeCost(index + 2, first)
            caseB = max(first, third) + self.computeCost(index + 2, second)
            caseC = max(first, second) + self.computeCost(index + 2, third)
            minCost = min(caseA, caseB, caseC)
        
        self.dpMemo[index][anchor] = minCost
        return minCost
    
    def minCost(self, nums):
        self.arr = nums
        self.arrSize = len(self.arr)
        self.dpMemo = [{} for _ in range(self.arrSize + 1)]
        
        if self.arrSize == 0:
            return 0
        
        if self.arrSize < 3:
            if self.arrSize == 1:
                return self.arr[0]
            else:
                return max(self.arr[0], self.arr[1])
        else:
            first, second, third = self.arr[0], self.arr[1], self.arr[2]
            optionA = max(second, third) + self.computeCost(3, first)
            optionB = max(first, third) + self.computeCost(3, second)
            optionC = max(first, second) + self.computeCost(3, third)
            ans = min(optionA, optionB, optionC)
        
        return int(ans)


