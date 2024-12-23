#Question : Preparing for the Olympiad
#Link to the question: https://codeforces.com/contest/2051/problem/A

"""
    Codeforces Round 995 (Div. 3)
    Author : Nishant Kumar
    Date : 22-12-2024
"""
 
 
def solve():
    n = int(input())
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))

    ans = arr1[-1]  
    for i in range(1, n):  
        if arr1[i-1] > arr2[i]:  
            ans += arr1[i-1] - arr2[i]

    print(ans)

for _ in range(int(input())):
    solve()

 
"""Author : Nishant Kumar"""
