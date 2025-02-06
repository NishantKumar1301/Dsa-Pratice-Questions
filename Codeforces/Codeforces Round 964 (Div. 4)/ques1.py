#Question :  A+B Again?
#Link to the question: https://codeforces.com/contest/1999/problem/A

for _ in range(int(input())):
    n =int(input())
    ans = 0
    while n > 0:
        ans += n %10
        n = n//10
    print(ans)