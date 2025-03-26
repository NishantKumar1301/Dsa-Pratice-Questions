#Question : Lost in the Fest!!
#Link to the question: https://www.codechef.com/problems/MDGT

# cook your dish here
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    ans =0
    idx= n-1
    h = arr[-1]
    while idx>0:
        maxi = max(arr[:idx])
        if h>maxi:
            break
        arr[idx],arr[idx-1]=arr[idx-1],arr[idx]
        idx-=1
        ans+=1
    print(ans)


