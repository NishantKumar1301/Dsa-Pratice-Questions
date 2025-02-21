#Question : Game With Sticks
#Link to the question: https://codeforces.com/contest/451/problem/A

n,m = map(int,input().split())
moves = min(n,m)
if moves %2==0:
    print("Malvika")
else:
    print("Akshat")

