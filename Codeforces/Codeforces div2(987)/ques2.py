"""
# How to check whether the array is sorted or not
arr1 =[1,2,3,4,5,6]
arr2 =[2,4,1,6,3]
is_sorted1= arr1 == sorted(arr1)
is_sorted2 = arr2 == sorted(arr2)
print(is_sorted1,is_sorted2)"""

#Link to the problem statement : https://codeforces.com/problemset/problem/2031/B

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    for i in range(0,n-1):
        if arr[i]-arr[i+1]==1:
            arr[i],arr[i+1]=arr[i+1],arr[i]


    is_sorted = arr == sorted(arr)
    print("Yes" if is_sorted else "No")