#Question : Minimum Number of Operations to Make X and Y Equal
#Link to the question: https://leetcode.com/problems/minimum-number-of-operations-to-make-x-and-y-equal/description/

from collections import deque
class Solution(object):
    def minimumOperationsToMakeEqual(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        if x<=y:
            return y-x
        LOW_LIMIT = 1 
        HIGH_LIMIT = x+11
        visited = [False]*HIGH_LIMIT
        visited[x]=True
        queue = deque()
        queue.append((x,0))
        while queue:
            num , steps = queue.popleft()
            if num==y:
                return steps
            if num>HIGH_LIMIT or num<LOW_LIMIT:
                continue
            if num%11==0 and not visited[num//11]:
                visited[num//11]=True
                queue.append((num//11,steps+1))
            if num%5==0 and not visited[num//5]:
                visited[num//5]=True
                queue.append((num//5,steps+1))
            if num-1>0 and not visited[num-1]:
                visited[num-1]=True
                queue.append((num-1,steps+1))
            if num+1<HIGH_LIMIT and not visited[num+1]:
                visited[num+1]=True
                queue.append((num+1,steps+1))
        return float('inf')