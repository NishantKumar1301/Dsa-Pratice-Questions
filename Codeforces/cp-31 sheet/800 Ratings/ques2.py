#Question : Line Problem
#Link to the question: https://codeforces.com/problemset/problem/1901/A

def solve():
    n,x = map(int, input().split())
    arr = list(map(int, input().split()))
    # Write your logic here
    gaps = []
    gaps.append(arr[0])
    for i in range(1,n):
        gaps.append(arr[i]-arr[i-1])
    gaps.append(2*(x-arr[-1]))
    ans = max(gaps)
    print(ans)


if __name__ == "__main__":
    for _ in range(int(input())):
        solve()
