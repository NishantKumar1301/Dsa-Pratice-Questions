#Question : Goals of Victory
#Link to the question: https://codeforces.com/problemset/problem/1877/A


def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    # Write your logic here
    print(-1*sum(arr))


if __name__ == "__main__":
    for _ in range(int(input())):
        solve()
