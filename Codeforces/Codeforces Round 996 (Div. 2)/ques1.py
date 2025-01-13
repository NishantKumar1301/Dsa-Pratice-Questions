#Question : Two Frogs
#Link to the question: https://codeforces.com/contest/2055/problem/A

def solve():
    n, a, b = map(int, input().split())
    if n == 2:
        print("NO")
    elif a % 2 != b % 2:  # If same parity, then also NO
        print("NO")
    else:
        if a == 1 and b == 2:
            print("NO")
        elif a == n and b == n - 1:
            print("NO")
        else:
            print("YES")

for _ in range(int(input())):
    solve()



