#Question : Shape Perimeter
#Link to the question: https://codeforces.com/contest/2056/problem/A




"""Author : Nishant Kumar"""
 
def perimeter_triangle():
    n, m = map(int, input().split())
    p, q = map(int, input().split())
    res = 0
 
    for _ in range(1, n):
        dx, dy = p, q
        p, q = map(int, input().split())
        p += dx
        q += dy
        res += abs(dx + m - p) + abs(dy + m - q)
    ans = n * 4 * m - (res * 2)
    print(ans)
 
test_case = int(input())
for _ in range(test_case):
    perimeter_triangle()
 
"""Author : Nishant Kumar"""