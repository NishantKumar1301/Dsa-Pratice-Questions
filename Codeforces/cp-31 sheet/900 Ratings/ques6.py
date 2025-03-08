#Question : Longest Divisors Interval
#Link to the question: https://codeforces.com/problemset/problem/1855/B

import math
for _ in range(int(input())):
    n = int(input())
    i = 1
    while n % i == 0:
        i += 1
    print(i-1 )
