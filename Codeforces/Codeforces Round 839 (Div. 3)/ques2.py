#Question : Matrix Rotation
#Link to the question: https://codeforces.com/contest/1772/problem/B

# cook your dish here
for _ in range(int(input())):
    a,b= map(int,input().split())
    c,d= map(int,input().split())
    if (b>a and d>c and c>a and d>b) or (a>c and b>d and d>c and b>a) or (c>d and a>b and b>d and a>c) or(d>b and c>a and a>b and c>d):
        print("YES")
    else:
        print("NO")

