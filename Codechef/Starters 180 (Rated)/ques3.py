#Question : Array Operations
#Link to the question: https://www.codechef.com/START180B/problems/OPAR?tab=ide

# cook your dish here
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    if n==1:
        print(arr[0])
        continue
    mid =(n-1)//2
    maxi = max(arr)
    extra = mid if any(arr[i] == maxi for i in range(0, n, 2)) else (mid - 1 if mid - 1 >= 0 else 0)
    print(maxi+extra)

