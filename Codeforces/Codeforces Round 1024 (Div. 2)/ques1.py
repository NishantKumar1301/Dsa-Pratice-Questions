#Question : Dinner Time
#Link to the question: https://codeforces.com/contest/2102/problem/A

# Contest: Codeforces Round 1024 (Div. 2)
# Date: May 11, 2025
# Author: Nishant Kumar

def solve():
    n,m,p,q = map(int, input().split())
    if (n%p==0 and (m != (n//p)*q)):
        print("NO")
    else:
        print("YES")
if __name__ == "__main__":
    for _ in range(int(input())):
        solve()
        
# Author: Nishant Kumar



