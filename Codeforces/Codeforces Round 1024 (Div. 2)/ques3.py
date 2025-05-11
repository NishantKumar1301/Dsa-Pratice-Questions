#Question : Mex in the Grid
#Link to the question: https://codeforces.com/contest/2102/problem/C

# Contest: Codeforces Round 1024 (Div. 2)
# Date: May 11, 2025
# Author: Nishant Kumar

def solve():
    n = int(input())
    arr = [[-1] * n for _ in range(n)]
    x = 0
    row = col = (n - 1) // 2
    if n % 2 == 0:
        row =col= n // 2 - 1
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    arr[row][col] = x
    x += 1
    cnt = 1
    while x < n * n:
        for i, (dx, dy) in enumerate(dirs):
            for _ in range(cnt):
                row += dx
                col += dy
                if 0 <= row < n and 0 <= col < n and arr[row][col] == -1:
                    arr[row][col] = x
                    x += 1
                    if x == n * n:
                        break
            if i % 2 == 1:
                cnt += 1
    for i in arr:
        print(" ".join(map(str, i)))

if __name__ == "__main__":
    for _ in range(int(input())):
        solve()


# Author: Nishant Kumar



