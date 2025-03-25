#Question : Place of the Olympiad
#Link to the question: https://codeforces.com/contest/2091/problem/D

# Contest: Codeforces Round 1013 (Div. 3)
# Date: March 25, 2025
# Author: Nishant Kumar

def helper(a, b):
    if a >= b:
        return b
    c = (b + 1) // (a + 1)
    c1 = min(c * a, b - c + 1)
    x = c + 1
    c2 = 0
    if x <= b + 1:
        c2 = min(x * a, b - x + 1)
    return max(c1, c2)

def solve():
    for _ in range(int(input())):
        a, b, c = map(int, input().split())
        left =1 
        right = b
        ans = b
        while left<=right:
            mid = (left+right)//2
            val = a*helper(mid,b)
            if val>=c:
                ans = mid
                right = mid-1
            else:
                left = mid+1
        print(ans)

if __name__ == "__main__":
    solve()

# Author: Nishant Kumar

