#Question : Bitwise ORs of Subarrays
#Link to the question: https://leetcode.com/problems/bitwise-ors-of-subarrays/
class Solution(object):
    def subarrayBitwiseORs(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        # s = set()
        # n = len(arr)
        # for i in range(n):
        #     for j in range(i,n):
        #         s.add(arr[i]|arr[j])
        # return len(s)
        n = len(arr)
        prev,curr,ans = set(),set(),set()
        for i in range(n):
            for num in prev:
                curr.add(num | arr[i])
                ans.add(num| arr[i])
            curr.add(arr[i])
            ans.add(arr[i])
            prev=curr
            curr = set()
        return len(ans)
        