#Question : Brogramming Contest
#Link to the question: https://codeforces.com/contest/2064/problem/A

# Contest: Codeforces Round 1005 (Div. 2)
# Date: February 16, 2025
# Author: Nishant Kumar
 
def solve():
    n = int(input())
    s= input().strip()
    ans = 0
    if s[0]=='1':
        ans+=1
    for i in range(1,n):
        if s[i]!=s[i-1]:
            ans+=1
    print(ans)

if __name__ == "__main__":
    for _ in range(int(input())):
        solve()
 
# Author: Nishant Kumar

