#Question : Card Game
#Link to the question: https://codeforces.com/contest/1999/problem/B


for _ in range(int(input())):
    a1,a2,b1,b2 = map(int,input().split())
    ans =0
    if (a1>b1 and a2>=b2) or (a1>=b1 and a2>b2):
        ans+=2
    if (a1>=b2 and a2>b1) or (a1>b2 and a2>=b1):
        ans +=2
    print(ans)