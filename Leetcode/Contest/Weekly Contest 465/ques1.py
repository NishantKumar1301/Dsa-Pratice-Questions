#Question : Restore Finishing Order
#Link to the question: https://leetcode.com/contest/weekly-contest-465/problems/restore-finishing-order/
class Solution(object):
    def recoverOrder(self, order, friends):
        """
        :type order: List[int]
        :type friends: List[int]
        :rtype: List[int]
        """
        n = len(order)
        ans = []
        is_frnd = [0]*(n+1)
        for x in friends:
            is_frnd[x]=1
        #[0,1,0,1,1,0]
        for x in order:
            if is_frnd[x]:
                ans.append(x)
            else:
                continue
        return ans