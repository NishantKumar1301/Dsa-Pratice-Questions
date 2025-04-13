#Question : Bobritto Bandito
#Link to the question: https://codeforces.com/contest/2094/problem/B

# cook your dish here
# Contest: Codeforces Round 1017 (Div. 4)
# Date: April 13, 2025
# Author: Nishant Kumar

def solve():
    n,m,l,r = map(int,input().split())
    left = -l
    right = r
    a = min(m,left)
    b = m-a
    print(-a,b)

if __name__ == "__main__":
    for _ in range(int(input())):
        solve()

# Author: Nishant Kumar


