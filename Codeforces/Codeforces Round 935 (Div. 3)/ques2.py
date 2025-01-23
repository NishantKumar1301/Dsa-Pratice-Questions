#Question : Fireworks
#Link to the question: https://codeforces.com/contest/1945/problem/B


# Contest: Codeforces Round 1000 (Div. 2)
# Date: 22-Jan-2025
# Author: Nishant Kumar

def solve():
    a,b,m = map(int,input().split())
    # Write your logic here
    ans = (m//a+1)+(m//b+1)
    print(ans)


if __name__ == "__main__":
    for _ in range(int(input())):
        solve()

# Author: Nishant Kumar
