#Question : Different Differences
#Link to the question: https://codeforces.com/contest/1772/problem/C

# cook your dish here
for _ in range(int(input())):
    k,n= map(int,input().split())
    start=diff=1
    for i in range(1,k+1):
        print(start,end=" ")
        if n -(start+diff)>=k-i-1:
            start+=diff
            diff+=1 
        else:
            start+=1 
    print()

