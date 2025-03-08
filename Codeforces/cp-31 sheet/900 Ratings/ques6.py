#Question : Longest Divisors Interval
#Link to the question: https://codeforces.com/problemset/problem/1855/B

import math

a = 1
for i in range(2, 51):
    a = math.lcm(a, i)
print(a)

for _ in range(int(input())):
    n = int(input())
    i = 1
    while n % i == 0:
        i += 1
    print(i )
