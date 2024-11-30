#Question : King Keykhosrow's Mystery
#Link to the question: https://codeforces.com/contest/2034/problem/A
def gcd(a,b):
    if b ==0:
        return a
    return gcd(b,a%b)
for _ in range(int(input())):
    a,b = map(int,input().split())
    hcf = gcd(a,b)
    ans = (a*b)//hcf
    print(ans)
    

