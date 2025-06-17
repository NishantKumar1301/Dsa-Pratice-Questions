#Question : D - 1709
#Link to the question: https://codeforces.com/contest/2121/problem/D

# Contest: Codeforces Round 1032 (Div. 3)
# Date: June 17, 2025
# Author: Nishant Kumar

def solve():
    n = int(input())
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))
    ans = []

    # Sort arr1 and record swaps
    for p in range(n):
        for i in range(n - 1):
            if arr1[i] > arr1[i + 1]:
                arr1[i], arr1[i + 1] = arr1[i + 1], arr1[i]
                ans.append((1, i + 1))

    # Sort arr2 and record swaps
    for p in range(n):
        for i in range(n - 1):
            if arr2[i] > arr2[i + 1]:
                arr2[i], arr2[i + 1] = arr2[i + 1], arr2[i]
                ans.append((2, i + 1))

    # Swap mismatched elements and record
    for i in range(n):
        if arr1[i] > arr2[i]:
            arr1[i], arr2[i] = arr2[i], arr1[i]
            ans.append((3, i + 1))

    print(len(ans))
    for num in ans:
        print(num[0], num[1])


if __name__ == "__main__":
    for _ in range(int(input())):
        solve()

# Author: Nishant Kumar
