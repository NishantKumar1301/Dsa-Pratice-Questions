#Question : Stair, Peak, or Neither?
#Link to the question: https://codeforces.com/problemset/problem/1950/A

for _ in range(int(input())):
    a,b,c = map(int,input().split())
    if a<b and b<c:
        print("STAIR")
    elif a<b and b>c:
        print("PEAK")
    else:
        print("NONE")

