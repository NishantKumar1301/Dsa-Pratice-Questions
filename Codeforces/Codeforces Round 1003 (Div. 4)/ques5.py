#Question :  Skibidus and Sigma
#Link to the question: https://codeforces.com/contest/2065/problem/D

# Contest: Codeforces Round 1003 (Div. 4)
# Date: February 9, 2025
# Author: Nishant Kumar

def solve():
    n,m = map(int, input().split())
    arr1,arr2=[],[]
    for _ in range(n):
        arr = list(map(int, input().split()))
        arr1.append(arr)
        arr2.append(sum(arr))
    sorted_arr = sorted(range(n),key=lambda i:-arr2[i])
    ans,sum_=0,0
    for idx in sorted_arr:
        for val in arr1[idx]:
            sum_+=val
            ans+=sum_
    print(ans)

if __name__ == "__main__":
    for _ in range(int(input())):
        solve()

# Author: Nishant Kumar
