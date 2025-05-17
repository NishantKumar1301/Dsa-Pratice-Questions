#Question : It's Time To Duel
#Link to the question: https://codeforces.com/contest/2109/problem/A

# Contest: Codeforces Round 1025 (Div. 2)
# Date: May 17, 2025
# Author: Nishant Kumar

def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    sum_ = sum(arr)
    if sum_ == n:
        print("YES")
        return
    flag = False
    for i in range(n - 1):
        if arr[i] == 0 and arr[i + 1] == 0:
            flag = True
            break
    print("YES" if flag else "NO")

if __name__ == "__main__":
    for _ in range(int(input())):
        solve()
