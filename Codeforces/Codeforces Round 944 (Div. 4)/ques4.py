#Question : Binary Cut
#Link to the question: https://codeforces.com/contest/1971/problem/D

for _ in range(int(input())):
    s= input()
    n = len(s)
    ans = 1
    flag = False
    for i in range(n-1):
        if s[i]!=s[i+1]:
            ans+=1
            if s[i]=='0' and s[i+1]=='1':
                flag = True
    if flag == True:
        ans-=1
    print(ans)