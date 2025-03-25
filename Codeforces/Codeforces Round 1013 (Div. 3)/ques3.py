#Question : Combination Lock
#Link to the question: https://codeforces.com/contest/2091/problem/C

# Contest: Codeforces Round 1013 (Div. 3)
# Date: March 25, 2025
# Author: Nishant Kumar

def solve():
    for _ in range(int(input())):
        n = int(input())
        if n%2==0:
            print(-1)
            continue
        for j in range(1,n+1):
            p = (2*j)%n
            if p==0:
                p=n
            print(p,end=" " if j!=n else "\n")
if __name__ == "__main__":
    solve()

# Author: Nishant Kumar

