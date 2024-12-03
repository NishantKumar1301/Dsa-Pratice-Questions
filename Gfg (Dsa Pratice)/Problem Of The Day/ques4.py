#Question : Majority Element
#Link to the question: https://www.geeksforgeeks.org/problems/majority-element-1587115620/1

from collections import Counter
class Solution:
    def majorityElement(self, arr):
        #Your code here
        count = Counter(arr)
        size = len(arr)
    
        for key, value in count.items():
            if value > size // 2:
                return key
        return -1