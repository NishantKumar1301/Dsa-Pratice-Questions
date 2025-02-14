#Question :  How Much Does Daytona Cost?
#Link to the question: https://codeforces.com/problemset/problem/1878/A


def solve():
    n,k = map(int, input().split())
    arr = list(map(int, input().split()))
    # Write your logic here
    flag = False
    for num in arr:
        if num == k:
            flag = True
            break
    print("YES" if flag else "NO")

if __name__ == "__main__":
    for _ in range(int(input())):
        solve()
