#Question : Beautiful Garden
#Link to the question: https://www.codechef.com/START182B/problems/DPF

# cook your dish here
for _ in range(int(input())):
    n,k,d = map(int,input().split())
    arr = list(map(int,input().split()))
    if n<=k:
        print(0)
    else:
        ans = 0
        arr.sort()
        for i in range(n-k):
            ans+=(d-1)//arr[i]+ 1 
        print(ans)

