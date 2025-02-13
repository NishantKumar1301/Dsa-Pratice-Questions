#Question : Median
#Link to the question: https://codeforces.com/contest/2032/problem/B


def solve():
    n, k = map(int, input().split())
    if n == 1 and k == 1:
        print(1)
        print(1)
        return 
    if k == 1 or k == n:
        print(-1)
        return 
    size = min(k - 1, n - k) * 2 + 1
    print(size)
    for i in range(1, min(k - 1, n - k) + 1):
        print(i, end=" ")
    print(k, end=" ")
    for i in range(1, min(k - 1, n - k) + 1):
        print(k + i, end=" ")
    print()  
if __name__ == "__main__":
    for _ in range(int(input())):
        solve()