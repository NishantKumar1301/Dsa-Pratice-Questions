#Question : Two Cards
#Link to the question: https://www.codechef.com/problems/TWOCARD

# cook your dish here
for _ in range(int(input())):
    n = int(input())
    arr1 = list(map(int,input().split()))
    arr2 = list(map(int,input().split()))
    maxval=0
    maxInd =-1
    for i in range(n):
        curval = max(arr1[i],arr2[i])
        if curval >maxval:
            maxval = curval
            maxInd=i 
    
    lrg =0
    second_lrg=0
    lrg_idx=-1
    second_idx=-1
    for i in range(n-1,-1,-1):
        if arr1[i] > lrg:
            second_lrg=lrg 
            second_idx = lrg_idx
            lrg = arr1[i]
            lrg_idx=i
        elif arr1[i] > second_lrg:
            second_lrg=arr1[i]
            second_idx =i 
            
    lrg = max(arr1[lrg_idx],arr2[lrg_idx])
    second_lrg = max(arr1[second_idx],arr2[second_idx])
    if lrg == second_lrg and maxval == lrg:
        print("NO")
    else:
        print("YES")
    



