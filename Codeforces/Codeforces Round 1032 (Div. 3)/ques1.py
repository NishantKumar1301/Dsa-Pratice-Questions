#Question : Letter Home
#Link to the question: https://codeforces.com/contest/2121/problem/A


# Contest: Codeforces Round 1032 (Div. 3)
# Date: June 17, 2025
# Author: Nishant Kumar

def solve():
    n,s =  map(int, input().split())
    arr = list(map(int, input().split()))
    a = arr[0]
    b = arr[n-1]
    ans = (b-a)+min(abs(s-a),abs(b-s))
    print(ans)


if __name__ == "__main__":
    for _ in range(int(input())):
        solve()

# Author: Nishant Kumar



