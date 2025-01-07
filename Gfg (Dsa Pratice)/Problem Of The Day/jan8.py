#Question : Count the number of possible triangles
#Link to the question: https://www.geeksforgeeks.org/problems/count-possible-triangles-1587115620/1

class Solution:
    def countTriangles(self, arr):
        arr.sort()
        n = len(arr)
        count = 0
        for i in range(n - 1, 1, -1):
            left = 0
            right = i - 1
            while left < right:
                if arr[left] + arr[right] > arr[i]:
                    count += (right - left)
                    right -= 1
                else:
                    left += 1
        
        return count

