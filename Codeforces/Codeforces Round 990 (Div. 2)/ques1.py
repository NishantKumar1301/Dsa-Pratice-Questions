#Question : Alyona and a Square Jigsaw Puzzle
#Link to the question: https://codeforces.com/contest/2047/problem/A



"""Author : Nishant Kumar"""

def solve():
    n = int(input())
    arr = list(map(int,input().split()))
    ans,total,j=0,0,1 #Start j = 1 Because j will be always odd
    for i in range(n):
        total+=arr[i]
        while j*j<total: #Observation : Happy only when total = perfect square of some odd index number 
            j+=2 
        if total==j*j:
            ans+=1
    print(ans)



for _ in range(int(input())):
    solve()

"""Author : Nishant Kumar"""