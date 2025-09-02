#Question : Maximum Average Pass Ratio
#Link to the question: https://leetcode.com/problems/maximum-average-pass-ratio/
from heapq import heappush ,heappop
class Solution(object):
    def calculate_increment(self,pass_student,total_student):
        current_average = pass_student / float(total_student)
        new_average =  (pass_student +1 ) / float(total_student+1)
        return new_average - current_average

    def maxAverageRatio(self, classes, extraStudents):
        """
        :type classes: List[List[int]]
        :type extraStudents: int
        :rtype: float
        """
        #Initialised the priority queue
        pq =[]
        for idx ,(pass_student , total_student) in enumerate(classes):
            increment = self.calculate_increment(pass_student,total_student)
            #Push the element by -increment bcoz python do not support  min heap so multiply increment by -1
            heappush(pq,(-increment,idx))
        
        #Pop the maximum incremented from the max heapq
        while extraStudents >0:
            idx = heappop(pq)[1]
            #Update the pass student and the total student of the particular index o the classes
            classes[idx][0]+=1
            classes[idx][1]+=1
            #Calculate the new incremented value and push it in the priority queue
            increment = self.calculate_increment(classes[idx][0],classes[idx][1])
            heappush(pq,(-increment,idx))
            extraStudents-=1
        
        #Find the final average and return the final_average / length of clsses
        final_average = sum(c[0]/float(c[1]) for c in classes)
        ans = final_average / float(len(classes))
        return ans
