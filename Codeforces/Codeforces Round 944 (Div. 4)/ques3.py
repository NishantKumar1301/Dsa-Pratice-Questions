#Question : Clocks And String
#Link to the question: https://codeforces.com/contest/1971/problem/C


for _ in range(int(input())):
    a,b,c,d = map(int,input().split())
    if a>b:
        a,b = b,a
    s1 = set()
    s2 = set()
    for i in range(a+1,b):
        s1.add(i)
    for i in range(1,13):
        if i not in s1 and i!=a and i!=b:
            s2.add(i)
    if (c in s1 and d in s2) or (c in s2 and d in s1):
        print("YES")
    else:
        print("NO")