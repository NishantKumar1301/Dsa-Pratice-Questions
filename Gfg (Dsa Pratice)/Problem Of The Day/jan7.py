#Question : Pair with given sum in a sorted array
#Link to the question: https://www.geeksforgeeks.org/problems/pair-with-given-sum-in-a-sorted-array4940/1

class Solution:
    def countPairs(self, arr, target):
        i = 0
        j = len(arr) - 1
        count = 0
        
        while i < j:
            if arr[i] + arr[j] > target:
                j -= 1
            elif arr[i] + arr[j] < target:
                i += 1
            else:
                count += 1
                ii = i + 1
                jj = j - 1
                while ii < j and arr[ii] == arr[i]:
                    count += 1
                    ii += 1
                while jj > i and arr[jj] == arr[j]:
                    count += 1
                    jj -= 1
                i += 1
                j -= 1
        
        return count


