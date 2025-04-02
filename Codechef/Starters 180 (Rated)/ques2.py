#Question : Shall we play a game
#Link to the question: https://www.codechef.com/START180B/problems/SWPG

# cook your dish here
MOD = 998244353
def solve(b,e,m):
    ans =1
    b %=m 
    while e>0:
        if e&1:
            ans =(ans*b)%m 
        b = (b*b)%m
        e>>=1
    return ans

for _ in range(int(input())):
    n = int(input())
    if n %2 ==1:
        ans = solve(2,n-1,MOD)
    else:
        ans = (3*solve(2,n-2,MOD))%MOD
    print(ans)


