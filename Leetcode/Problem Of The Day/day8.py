#Question : Maximum Number of Integers to Choose From a Range I
#Link to the question: https://leetcode.com/problems/maximum-number-of-integers-to-choose-from-a-range-i/description/?envType=daily-question&envId=2024-12-06

class Solution(object):
    def maxCount(self, banned, n, maxSum):
        """
        :type banned: List[int]
        :type n: int
        :type maxSum: int
        :rtype: int
        """
        banned_set = set(banned)  
        total_sum = 0  
        count = 0  

        for i in range(1, n + 1):
            if i in banned_set:
                continue  
            total_sum += i
            if total_sum > maxSum:
                break  
            count += 1

        return count
        

