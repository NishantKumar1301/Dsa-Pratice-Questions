#Question : Setting up Camp
#Link to the question: https://codeforces.com/contest/1945/problem/A

# Contest: Codeforces Round 935 (Div. 3)
# Date: 24-Jan-2025
# Author: Nishant Kumar
import math
def solve():
    a,b,c = map(int,input().split())
    # Write your logic here
    ans = a
    ans+=b//3 
    b%=3
    if b>0 and 3-b>c:
        print(-1)
        return 
    
    if b > 0 :
        ans+=1 
        c-=(3-b)
    b=0
    # ans+=(c+2)//3 # ceil division of c/b = c+b-1//b , here it is ceil of c/3 is required 
    ans+= math.ceil(c/3)
    print(ans)


if __name__ == "__main__":
    for _ in range(int(input())):
        solve()

# Author: Nishant Kumar



