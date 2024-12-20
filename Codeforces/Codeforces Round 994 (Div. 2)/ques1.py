#Question :MEX Destruction
#Link to the question: https://codeforces.com/contest/2049/problem/A

"""Author : Nishant Kumar"""

# def solve():
#     n = int(input())
#     arr = list(map(int,input().split()))
#     ans = 0 
#     flag = False 
#     for num in arr:
#         if num!=0:
#             if flag==False:
#                 ans+=1
#                 flag =True
#         if num==0:
#             flag = False 
#     print(2 if ans>2 else ans)


# for _ in range(int(input())):
#     solve()

# """Author : Nishant Kumar"""

#Second Approach :
#If all elements are 0 then answer is 0 
#If no zero is between the first_non zero to last_non_zero then ans=1 
#in rest of the cases answer is 2 

"""Author : Nishant Kumar"""

def solve():
    n = int(input())
    arr = list(map(int,input().split()))
    first_non_zero_idx =last_non_zero_idx=-1
    for i in range(n):
        if arr[i]!=0:
            if first_non_zero_idx==-1:
                first_non_zero_idx=i 
            last_non_zero_idx =i 
    #Case 1: ALl elements are 0 
    if all(x==0 for x in arr):
        print(0) 
    #Case 2: If no zero is present in between first and last non_zero index
    if all(arr[i]!=0 for i in range(first_non_zero_idx,last_non_zero_idx+1)):
        print("YES")
    print(2)



for _ in range(int(input())):
    solve()

"""Author : Nishant Kumar"""