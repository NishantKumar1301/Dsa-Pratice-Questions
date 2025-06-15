#Question : Max Difference You Can Get From Changing an Integer
#Link to the question: https://leetcode.com/problems/max-difference-you-can-get-from-changing-an-integer/
class Solution(object):
    def maxDiff(self, num):
        """
        :type num: int
        :rtype: int
        """
        s1 = str(num)
        s2 = str(num)
        for char in s1:
            if char!='9':
                s1 = s1.replace(char,'9')
                break
        for i,char in enumerate(s2):
            if i==0:
                if char!='1':
                    s2 =s2.replace(char,'1')
                    break
            elif char!='0' and char!=s2[0]:
                s2 = s2.replace(char,'0')
                break
        return int(s1)-int(s2)
