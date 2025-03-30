#Question :  Lady Bug
#Link to the question: https://codeforces.com/contest/2092/problem/B

# Contest: Codeforces Round 1014 (Div. 2)
# Date: March 29, 2025
# Author: Nishant Kumar

def solve():
    n = int(input())
    a = input()
    b = input()
    a1 = 0
    a2 = 0
    for i in range(n):
        if i % 2 == 0:
            if a[i] == '1': a1 += 1
            if b[i] == '1': a2 += 1
        else:
            if a[i] == '1': a2 += 1
            if b[i] == '1': a1 += 1
    
    b1 = n // 2
    b2 = (n + 1) // 2
    
    flag = a1 <= b1 and a2 <= b2
    
    print("YES" if flag else "NO")

if __name__ == "__main__":
    for _ in range(int(input())):
        solve()

# Author: Nishant Kumar


