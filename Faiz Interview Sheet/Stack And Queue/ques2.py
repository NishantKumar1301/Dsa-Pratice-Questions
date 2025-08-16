#Question : Implement Queue using Stacks
#Link to the question: https://leetcode.com/problems/implement-queue-using-stacks/

class MyQueue(object):

    def __init__(self):
        self.stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack.append(x)
        for _ in range(len(self.stack)-1):
            prev = self.stack.pop(0)
            self.stack.append(prev)
        

    def pop(self):
        """
        :rtype: int
        """
        if len(self.stack)==0:
            return None
        return self.stack.pop()
        

    def peek(self):
        """
        :rtype: int
        """
        if len(self.stack)==0:
            return None
        return self.stack[-1]
        

    def empty(self):
        """
        :rtype: bool
        """
        if len(self.stack)==0:
            return True
        else:
            return False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()