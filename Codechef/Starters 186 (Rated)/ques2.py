#Question : Jump A or B
#Link to the question: https://www.codechef.com/START186B/problems/JUMPAB

# cook your dish here
for _ in range(int(input())):
    n, m, a, b = map(int, input().split())
    upper = m - b * n
    lower = a - b
    if m % n == 0 and (m // n == a or m // n == b):
        print("YES")
        continue
    if m < n:
        print("NO")
        continue
    if lower == 0 or upper % lower != 0:
        print("NO")
        continue
    z = upper // lower
    if 0 <= z <= n:
        print("YES")
    else:
        print("NO")
    