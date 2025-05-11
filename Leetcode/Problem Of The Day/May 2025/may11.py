#Question : Three Consecutive Odds
#Link to the question: https://leetcode.com/problems/three-consecutive-odds/description/?envType=daily-question&envId=2025-05-11

class Solution(object):
    def threeConsecutiveOdds(self, arr):
        """
        :type arr: List[int]
        :returnType: bool
        """
        n = len(arr)
        cnt=0
        for i in range(n):
            if arr[i]%2!=0:
                cnt+=1
                if cnt==3:
                    return True
            else:
                cnt =0
        return False
