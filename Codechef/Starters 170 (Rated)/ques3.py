#Question : Monster Monster
#Link to the question: https://www.codechef.com/START170B/problems/KO_MON

# cook your dish here
for _ in range(int(input())):
    n,x = map(int,input().split())
    arr = list(map(int,input().split()))
    arr.sort(reverse=True)
    ans =0
    for i in range(n):
        req= arr[i]+x*i 
        ans = max(ans,req)
    print(ans)


