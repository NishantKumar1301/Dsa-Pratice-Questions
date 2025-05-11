#Question : The Picky Cat
#Link to the question: https://codeforces.com/contest/2102/problem/B

# Contest: Codeforces Round 1024 (Div. 2)
# Date: May 11, 2025
# Author: Nishant Kumar

def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    for i in range(n):
        if abs(arr[0])>abs(arr[i]):
            cnt += 1
    if cnt>n//2:
        print("NO")
    else:
        print("YES")
    
if __name__ == "__main__":
    for _ in range(int(input())):
        solve()

# Author: Nishant Kumar



