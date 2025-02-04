#Question : Maximum Rounding
#Link to the question: https://codeforces.com/contest/1857/problem/B


def solve(s):
    s= "0"+s
    n = len(s)
    zeros = n
    s= list(s)
    for i in range(n-1,-1,-1):
        if s[i]>='5':
            s[i]='0'
            zeros = i
            j=i-1
            
            while s[j]=='9':
                s[j]='0'
                j-=1
            
            s[j]=str(int(s[j])+1)
    for i in range(zeros,n):
        s[i]='0'
    
    
    ans = "".join(s)
    
    if ans[0]=='0':
        ans = ans[1:]
    
    return ans

for _ in range(int(input())):
    s= input().strip()
    print(solve(s))
    
