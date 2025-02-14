#Question : Jagged Swaps
#Link to the question: https://codeforces.com/problemset/problem/1896/A

def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    # Write your logic here
    if arr[0]==1:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    for _ in range(int(input())):
        solve()
