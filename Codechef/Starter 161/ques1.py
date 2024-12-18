#Question : Selling Donuts
#Link to the question: https://www.codechef.com/problems/DONUTSELL

# cook your dish here
for _ in range(int(input())):
    n,m = map(int,input().split())
    arr1 = list(map(int,input().split()))
    arr2 = list(map(int,input().split()))
    ans =0
    for i in range(m):
        if(arr1[arr2[i]-1]>0):
            arr1[arr2[i]-1]-= 1
        else:
            ans+=1 
    print(ans)
    


