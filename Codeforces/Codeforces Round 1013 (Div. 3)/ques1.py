#Question : Olympiad Date
#Link to the question: https://codeforces.com/contest/2091/problem/A

# Contest: Codeforces Round 1013 (Div. 3)
# Date: March 25, 2025
# Author: Nishant Kumar

def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    ans =0
    p=[0]*10
    for i in range(n):
        p[arr[i]]+=1
        if p[0]>=3 and p[1]>=1 and p[2]>=2 and p[3]>=1 and p[5]>=1:
            ans=i+1
            break
    print(ans)
if __name__ == "__main__":
    for _ in range(int(input()) ):
        solve()
# Author: Nishant Kumar

