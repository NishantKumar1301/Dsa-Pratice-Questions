#Question : Those Who Are With Us
#Link to the question: https://codeforces.com/contest/2121/problem/C

# Contest: Codeforces Round 1032 (Div. 3)
# Date: June 17, 2025
# Author: Nishant Kumar

def solve():
    n, m = map(int, input().split())
    arr= []
    ans = 0
    for _ in range(n):
        row = list(map(int, input().split()))
        arr.append(row)
        ans = max(ans, max(row))
    tmp = []
    for i in range(n):
        for j in range(m):
            if arr[i][j] == ans:
                tmp.append((i, j))
    flag = False
    for i in range(n):
        s = set()
        for a, b in tmp:
            if a != i:
                s.add(b)
                if len(s) > 1:
                    break
        if len(s) <= 1:
            flag = True
            break
    print(ans - 1 if flag else ans)
if __name__ == "__main__":
    for _ in range(int(input())):
        solve()

# Author: Nishant Kumar
