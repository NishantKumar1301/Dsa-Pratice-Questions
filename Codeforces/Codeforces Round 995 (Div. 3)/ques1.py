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
    ans=0
    
    for i in range(n):
        if i + 1 < n and arr1[i] >= arr2[i + 1]:
            ans += (arr1[i] - arr2[i + 1])
        elif i == n - 1:
            ans += arr1[i]
    print(ans)
    
 
for _ in range(int(input())):
    solve()
 
"""Author : Nishant Kumar"""
