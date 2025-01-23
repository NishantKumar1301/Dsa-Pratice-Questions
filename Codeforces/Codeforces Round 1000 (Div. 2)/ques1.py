#Question : Minimal Coprime
#Link to the question: https://codeforces.com/contest/2063/problem/A

# Contest: Codeforces Round 1000 (Div. 2)
# Date: 22-Jan-2025
# Author: Nishant Kumar

from math import gcd

def solve():
    l,r= map(int,input().split())
    if l==1 and r==1:
        print(1)
        return 
    print(r-l)

if __name__ == "__main__":
    for _ in range(int(input())):
        solve()

# Author: Nishant Kumar


