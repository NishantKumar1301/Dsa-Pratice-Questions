#Question : Clockwork 
#Link to the question:  https://codeforces.com/contest/2062/problem/B

# Contest: Ethflow Round 1 (Codeforces Round 1001, Div. 1 + Div. 2)
# Date: 26-Jan-2025
# Author: Nishant Kumar
 
def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    flag =True
    for i in range(n):
        if arr[i]<=2*(n-i-1) or arr[i]<=2*i:
            flag = False
    if flag:
        print("YES")
    else:
        print("NO")
 
 
if __name__ == "__main__":
    for _ in range(int(input())):
        solve()
 
# Author: Nishant Kumar

