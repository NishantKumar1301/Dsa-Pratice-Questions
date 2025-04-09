#Question : Rotating the Box
#Link to the question: https://leetcode.com/problems/rotating-the-box/description/?envType=daily-question&envId=2024-11-23

class Solution(object):
    def rotateTheBox(self, box):
        """
        :type box: List[List[str]]
        :rtype: List[List[str]]
        """
        m = len(box)
        n = len(box[0])
        for row in box:
            pos = n-1
            for col in range(n-1,-1,-1):
                if row[col]=="#":
                    row[col]="."
                    row[pos]="#"
                    pos-=1
                elif row[col]=="*":
                    pos=col-1
        #Step2: Find the rotated array
        rotated =[[box[row][col] for row in range(m)]for col in range(n)]

        #STep3 : Reverse ech row of the rotted array

        for row in rotated:
            row.reverse()
        
        return rotated

        