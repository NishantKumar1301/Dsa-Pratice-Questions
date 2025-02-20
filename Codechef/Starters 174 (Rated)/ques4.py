#Question : Mystic Slimes
#Link to the question: https://www.codechef.com/problems/MYSSLIME

# cook your dish here
import sys

def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    if n == 2:
        print(abs(arr[0] - arr[1]))
        return

    maxi = max(arr)
    arr1 = [i for i in range(n) if arr[i] == maxi]
    ans = -1

    for i in arr1:
        if i == 0 or i == n - 1:
            ans = maxi
            break
        if i == 1 and (n - i - 1) == 1:
            ans = max(ans, maxi - arr[0] - arr[n - 1])
        elif i == 1 and (n - i - 1) > 1:
            ans = max(ans, maxi - arr[0])
        elif i > 1 and (n - i - 1) == 1:
            ans = max(ans, maxi - arr[n - 1])
        else:
            ans = max(ans, maxi)
            break

    maxi = max(ans, arr[0], arr[n - 1])
    for i in range(2, n - 2):
        maxi = max(maxi, arr[i])

    if n == 3:
        val = arr[1] - arr[0] - arr[2]
        maxi = max(maxi, val)
    else:
        first = arr[1] - arr[0]
        second = arr[n - 2] - arr[n - 1]
        maxi = max(maxi, first, second)

    print(maxi)

def main():
    for _ in range(int(sys.stdin.readline().strip())):
        solve()

if __name__ == "__main__":
    main()


