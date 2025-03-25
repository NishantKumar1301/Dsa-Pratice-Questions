#Question : Team Training
#Link to the question: https://codeforces.com/contest/2091/problem/B

# Contest: Codeforces Round 1013 (Div. 3)
# Date: March 25, 2025
# Author: Nishant Kumar
def solve():
    n,x= map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort(reverse=True)
    ans =0
    mini = float('inf')
    cnt =0
    for num in arr:
        cnt+=1
        mini = min(mini,num)
        if cnt*mini>=x:
            ans+=1
            cnt=0
            mini=float('inf')
    print(ans)

if __name__ == "__main__":
    for _ in range(int(input())):
        solve()

# Author: Nishant Kumar

