#Question : Red-Blue Sort
#Link to the question: https://www.codechef.com/problems/RBGM

# cook your dish here
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    cnt =0
    for i in range(n):
        if arr[i]==i+1:
            cnt+=1
    
    if cnt == n:
        print(n)
    elif cnt >=1:
        print(n-1)
    else:
        if n>=2 :
            print(n-2)
        else:
            print(0)


