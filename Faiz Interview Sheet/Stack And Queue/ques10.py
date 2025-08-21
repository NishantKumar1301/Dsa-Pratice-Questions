#Question : Asteroid Collision
#Link to the question: https://leetcode.com/problems/asteroid-collision/
class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        stack = []
        for num in asteroids:
            if num>0:
                stack.append(num)
            else:
                while len(stack)>0 and stack[-1]>0 and stack[-1]<abs(num):
                    stack.pop()
                if len(stack)>0 and stack[-1]==abs(num):
                    stack.pop()
                    continue
                if len(stack)==0 or stack[-1]<0:
                    stack.append(num)
        return stack