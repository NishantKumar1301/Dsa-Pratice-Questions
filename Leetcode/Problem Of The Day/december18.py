#Question : Construct String With Repeat Limit
#Link to the question: https://leetcode.com/problems/construct-string-with-repeat-limit/?envType=daily-question&envId=2024-12-17

from collections import Counter
from heapq import heappush , heappop
class Solution(object):
    def repeatLimitedString(self, s, repeatLimit):
        """
        :type s: str
        :type repeatLimit: int
        :rtype: str
        """
        #Step1 : Find the count of every character of the string
        freq = Counter(s)
        pq =[] #In python min heap is initiallised for using it as a max heap we will multiply by -1
        for char , count in freq.items():
            heappush(pq,(-ord(char),count)) #Use -ord(char) for acting the heap as a max heap
        
        #Step 2 : Pop the element from the max heap
        ans =""
        while pq:
            current_element = heappop(pq)
            current_char = chr(-current_element[0])
            count = min(repeatLimit,current_element[1])
            ans+=current_char*count
            current_element = (current_element[0],current_element[1]-count)
            if current_element[1]>0:
                
                #If the priority queue is empty then break
                if not pq:
                    break
                
                #Pop the next element
                next_element = heappop(pq)
                next_char = chr(-next_element[0])
                ans += next_char
                next_element = (next_element[0],next_element[1]-1)
                
                #If the count of the next element have more occurrences
                if next_element[1] > 0:
                    heappush(pq,next_element)
                
                #Push the current element in the priority queue i the count is still greater than 1
                heappush(pq,current_element)
        return ans

