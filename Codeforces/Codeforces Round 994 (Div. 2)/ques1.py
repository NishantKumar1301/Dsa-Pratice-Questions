#Question :MEX Destruction
#Link to the question: https://codeforces.com/contest/2049/problem/A

"""Author : Nishant Kumar"""

def solve():
    n = int(input())
    arr = list(map(int,input().split()))
    ans = 0 
    flag = False 
    for num in arr:
        if num!=0:
            if flag==False:
                ans+=1
                flag =True
        if num==0:
            flag = False 
    print(2 if ans>2 else ans)


for _ in range(int(input())):
    solve()

"""Author : Nishant Kumar"""