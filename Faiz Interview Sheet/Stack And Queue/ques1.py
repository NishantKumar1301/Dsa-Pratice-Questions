#Question : Implement Stack using Queues
#Link to the question: https://leetcode.com/problems/implement-stack-using-queues/

from collections import deque
class MyStack(object):

    def __init__(self):
        self.queue = deque()

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        
        #Now reverse the queue till length - 1 to behave it like a stack 
        """
        queue = [1],  stack = [1]
        push 2 -> queue = [1,2] - perform iteration [2,1]
        push 3 -> queue = [2,1,3]  - perform itertion [3,2,1]
        push 4 -> queue = [3,2,1,4] - perform iteration [4,3,2,1] queue.popleft = 4 which is lifo
        """
        self.queue.append(x)
        for i in range(len(self.queue)-1):
            x = self.queue.popleft()
            self.queue.append(x)
        

    def pop(self):
        """
        :rtype: int
        """
        if len(self.queue)==0:
            return None
        return self.queue.popleft()
        

    def top(self):
        """
        :rtype: int
        """
        if len(self.queue)==0:
            return None
        return self.queue[0]
        

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.queue)==0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()