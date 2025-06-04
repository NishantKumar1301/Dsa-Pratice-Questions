#Question : Create Binary String
#Link to the question:https://www.codechef.com/START189B/problems/CREATEBINSTR
# cook your dish here
for _ in range(int(input())):
    n,a,b,c,d = map(int,input().split())
    maxi = max(c, d)
    ans = 0
    for i in range(n + 1):
        j = n - i
        dia = i* j
        t = a * i + b * j + maxi * dia
        if t > ans:
            ans = t
    print(ans)