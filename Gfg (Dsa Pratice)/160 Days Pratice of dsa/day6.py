#Question : Majority Element II
#Link to the question: https://www.geeksforgeeks.org/batch/gfg-160-problems/track/arrays-gfg-160/problem/majority-vote

class Solution:
    def findMajority(self, arr):
        n = len(arr)
        threshold = n // 3

        # Step 1: Count the frequency of each element
        freq = {}
        for num in arr:
            if num in freq:
                freq[num]+=1
            else:
                freq[num]=1
        # Step 2: Filter elements with frequency > n/3
        res = []
        for key, value in freq.items():
            if value > threshold:
                res.append(key)

        # Step 3: Sort the result
        res.sort()

        # Step 4: Return at most 2 elements
        return res[:2]

