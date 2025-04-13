#Question : Tung Tung Sahur
#Link to the question: https://codeforces.com/contest/2094/problem/D

# Contest: Codeforces Round 1017 (Div. 4)
# Date: April 13, 2025
# Author: Nishant Kumar

def solve():
    p = input()
    s= input()
    if p==s:
        print("YES")
        return
    flag = True
    n,m,i,j = len(p),len(s),0,0
    while i<n and j<m:
        a = p[i]
        b = s[j]
        if a!=b:
            flag = False
            break
        cnt1=cnt2=0
        while i<n and p[i]==a:
            cnt1+=1
            i+=1
        while j<m and s[j]==b:
            cnt2+=1
            j+=1
        if cnt1>cnt2 or cnt2>2*cnt1:
            flag = False
            break
    if i==n and j==m and flag:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    for _ in range(int(input())):
        solve()

# Author: Nishant Kumar

