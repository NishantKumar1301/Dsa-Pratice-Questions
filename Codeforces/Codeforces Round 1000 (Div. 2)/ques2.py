#Question : Subsequence Update
#Link to the question: https://codeforces.com/contest/2063/problem/B

# Contest: Codeforces Round 1000 (Div. 2)
# Date: 22-Jan-2025
# Author: Nishant Kumar

def solve():
    n, l, r = map(int, input().split())
    arr = list(map(int, input().split()))
    l -= 1  
    r -= 1
    arr1 = arr[l:r+1]
    arr1.sort(reverse=True) 
    left = arr[:l]
    right = arr[r+1:]
    left.sort()  
    right.sort()  

    sum1 =sum2= 0
    size1 = min(len(arr1), len(left))
    for i in range(size1):
        if left[i] < arr1[i]:
            sum1 += left[i]
        else:
            sum1 += arr1[i]
    sum1 += sum(arr1[size1:])  

    size2 = min(len(arr1), len(right))
    for i in range(size2):
        if right[i] < arr1[i]:
            sum2 += right[i]
        else:
            sum2 += arr1[i]
    sum2 += sum(arr1[size2:])  

    print(min(sum1, sum2))

if __name__ == "__main__":
    for _ in range(int(input())):
        solve()
 
# Author: Nishant Kumar


