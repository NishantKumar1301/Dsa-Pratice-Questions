#Link to the problem : https://codeforces.com/contest/2014/problem/A
for _ in range(int(input())):
    n,k = map(int,input().split())
    arr = list(map(int,input().split()))
    score =0
    ans=0
    for i in range(n):
        if arr[i]>=k:
            score+=arr[i]
        if arr[i]==0 and score >0:
            ans+=1
            score-=1
                
    print(ans)
    