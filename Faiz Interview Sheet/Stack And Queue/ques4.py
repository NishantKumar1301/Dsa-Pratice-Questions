#Question : Min Stack
#Link to the question: https://leetcode.com/problems/min-stack/

class MinStack(object):

    def __init__(self):
        self.stack = []
        self.mini = float('inf')

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        if len(self.stack)==0:
            self.stack.append(val)
            self.mini = val
        else:
            if val>self.mini:
                self.stack.append(val)
            else:
                self.stack.append(2*val-self.mini)
                self.mini = val #Mini stores the top
        

    def pop(self):
        """
        :rtype: None
        """
        if len(self.stack)==0:
            return None
        val = self.stack.pop()
        if val<self.mini:
            self.mini = 2*self.mini-val

    def top(self):
        """
        :rtype: int
        """
        val = self.stack[-1]
        if val<self.mini:
            return self.mini
        return val

    def getMin(self):
        """
        :rtype: int
        """
        return self.mini
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()