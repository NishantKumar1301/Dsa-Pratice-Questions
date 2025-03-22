#Question : Serval and String Theory
#Link to the question: https://codeforces.com/contest/2085/problem/A

def solve(p):
    n = len(p)
    for i in range(n // 2):
        if p[i] != p[n - 1 - i]:
            return p[i] < p[n - 1 - i]
    return False

for _ in range(int(input())):
    n, p = map(int, input().split())
    s = input()
    
    if solve(s):
        print("YES")
        continue
    
    flag = True
    for i in range(1, n):
        if s[i] != s[0]:
            flag = False
            break
    
    if n == 1 or flag:
        print("NO")
    else:
        if p >= 1:
            print("YES")
        else:
            print("NO")


