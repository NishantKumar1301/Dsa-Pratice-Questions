#Question : qUiRkY qUesTs (Easy)
#Link to the question: https://www.codechef.com/START170B/problems/N3AL_

# cook your dish here
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    arr.sort()
    total = sum(arr)
    ans = total
    temp = total
    for i in range(n):
        temp-=arr[i]
        ans = max(ans,temp+(i+1)**2)
    ans = max(ans,n**2)
    print(ans)


