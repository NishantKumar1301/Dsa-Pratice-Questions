#Question : Ninja’s Training
#Link to the question:  https://www.naukri.com/code360/problems/ninja%E2%80%99s-training_3621003

#Method1 : Using Memoization(Top-Down)

class Solution:
    def helper(self,day,last,points,dp):
        if dp[day][last]!=-1:
            return dp[day][last]
        if day ==0:
            maxi= 0
            for i in range(3):
                if i != last:
                    maxi = max(maxi,points[0][i])
                    dp[day][last]=maxi
            return dp[day][last]
        maxi =0
        for i in range(3):
            if i != last:
                point = points[day][i]+self.helper(day-1,i,points,dp)
                maxi = max(point,maxi)
        dp[day][last]= maxi
        return dp[day][last]
        
        
    def maximumPoints(self, arr):
        # Code here
        n = len(arr)
        #Dp array size is n*4
        dp = [[-1 for j in range(4)] for i in range(n)]
        return self.helper(n-1,3,arr,dp)


#Method 2 : Using Tabulation 

def ninjaTraining(n: int, points: List[List[int]]) -> int:

    # Write your code here.
    dp = [[-1 for j in range(4)] for i in range(n)] #SIze of dp =n*4
    dp[0][0]=max(points[0][1],points[0][2])
    dp[0][1]=max(points[0][0],points[0][2])
    dp[0][2]=max(points[0][1],points[0][0])
    dp[0][3]=max(points[0][0],points[0][1],points[0][2])

    for day in range(1,n): # Total rows = day = n
        for last in range(4): # Last = 0,1,2,3
            maxi = 0
            for task in range(3): #Task = 0,1,2
                if task!=last:
                    point = points[day][task]+dp[day-1][task]
                    maxi = max(maxi,point)
            dp[day][last]= maxi
    
    return dp[n-1][3]


