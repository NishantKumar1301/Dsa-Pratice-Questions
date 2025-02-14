#Question : Ambitious Child
#Link to the question: https://codeforces.com/problemset/problem/1866/A


def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    # Write your logic here
    for i in range(n):
        if arr[i]<0:
            arr[i]=-arr[i]
    mini = min(arr)
    print(mini)


if __name__ == "__main__":
    solve()
