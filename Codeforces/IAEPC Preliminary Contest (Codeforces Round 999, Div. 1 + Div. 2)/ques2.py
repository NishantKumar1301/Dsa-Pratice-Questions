#Question : Kevin and Geometry
#Link to the question: https://codeforces.com/contest/2061/problem/B
#2*c>b-1

"""Author : Nishant Kumar"""

def solve():
    n = int(input())
    arr = list(map(int,input().split()))
    arr.sort()
    ind=-1 
    for i in range(n-1):
        if arr[i]==arr[i+1]:
            ind=i 
            break
    
    if ind ==-1:
        print(ind)
        return 
    
    c= arr[ind]
    arr.pop(ind+1)
    arr.pop(ind)
    #Calculate the new length after poping the 2 elements
    n = len(arr)
    for i in range(n-1):
        a=arr[i]
        b = arr[i+1]
        if 2*c>b-a:
            print(c,c,arr[i],arr[i+1])
            return 
    
    print(-1)



for _ in range(int(input())):
    solve()

"""Author : Nishant Kumar"""




