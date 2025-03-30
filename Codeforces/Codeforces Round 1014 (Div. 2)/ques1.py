#Question : Kamilka and the Sheep
#Link to the question: https://codeforces.com/contest/2092/problem/A

# Contest: Codeforces Round 1014 (Div. 2)
# Date: March 29, 2025
# Author: Nishant Kumar

def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    mini = min(arr)
    maxi = max(arr)
    print(maxi-mini)

if __name__ == "__main__":
    for _ in range(int(input())):
        solve()

# Author: Nishant Kumar

