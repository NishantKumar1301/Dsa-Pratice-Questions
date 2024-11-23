#Question : Minimize the Heights II
#Link to the question: https://www.geeksforgeeks.org/batch/gfg-160-problems/track/arrays-gfg-160/problem/minimize-the-heights3351

class Solution:
    def getMinDiff(self, arr, k):
        n = len(arr)
        arr.sort()
        ans = arr[-1] - arr[0]  
        smallest = arr[0] + k
        largest = arr[-1] - k

        for i in range(n - 1):
            maxi = max(largest, arr[i] + k)
            mini = min(smallest, arr[i + 1] - k)
            if mini < 0:
                continue
            ans = min(ans, maxi - mini)
        
        return ans

