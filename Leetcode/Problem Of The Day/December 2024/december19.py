#Question : Max Chunks To Make Sorted 
#Link to the question: https://leetcode.com/problems/max-chunks-to-make-sorted/description/?envType=daily-question&envId=2024-12-19

class Solution(object):
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        #Approach 1: If the array element is all different
        # maxi = float("-inf")
        # ans =0
        # for i in range(len(arr)):
        #     maxi = max(maxi,arr[i])
        #     if i==maxi:
        #         ans+=1
        # return ans
        
        #Approach 2: Optimal => If there is duplicate in the array
        
        stack =[]
        for num in arr:
            largest = num 
            while stack and num<stack[-1]:
                largest = max(largest,stack.pop())
            stack.append(largest)
        return len(stack)


        

