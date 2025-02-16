#Question : Remove the Ends
#Link to the question: https://codeforces.com/contest/2064/problem/C

# Contest: Codeforces Round 1005 (Div. 2)
# Date: February 16, 2025
# Author: Nishant Kumar
 
 
def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    # Write your logic here
    p =[0]*(n+1)
    s = [0]*(n+1)
    for i in range(n):
        p[i+1]=p[i]+max(0,arr[i])
    for i in range(n-1,-1,-1):
        s[i]=s[i+1]+max(0,-arr[i])
    ans =0
    for i in range(n+1):
        ans = max(ans,p[i]+s[i])
    print(ans)
 
 
if __name__ == "__main__":
    for _ in range(int(input())):
        solve()
 
# Author: Nishant Kumar

