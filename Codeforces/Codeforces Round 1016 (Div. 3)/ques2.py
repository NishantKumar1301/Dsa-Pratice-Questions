#Question : Expensive Number
#Link to the question: https://codeforces.com/contest/2093/problem/B

for _ in range(int(input())):
    n = input().strip()
    c =d=0
    for char in n :
        if char =='0':
            c+=1
        else:
            d = max(d,c+1)
    ans = (len(n)-d)
    print(ans)

