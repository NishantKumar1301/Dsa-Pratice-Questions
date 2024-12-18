#Question :Stable Array
#Link to the question: https://www.codechef.com/problems/STABARR

# cook your dish here
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    max_suffix = [None]*n
    stable =[None]*n 
    max_suffix[n-1]=arr[n-1]
    for i in range(n-2,-1,-1):
        max_suffix[i]=max(arr[i],max_suffix[i+1])
    stable[n-1]=0
    for i in range(n-2,-1,-1):
        if max_suffix[i]==arr[i]:
            stable[i]=0
        else:
            stable[i]=stable[i+1]+1
    ans = 0
    for i in range(n):
        ans = max(ans,stable[i])
    print(ans)


