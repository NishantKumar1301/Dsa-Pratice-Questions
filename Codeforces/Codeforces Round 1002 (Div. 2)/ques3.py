#Question : Customer Service
#Link to the question: https://codeforces.com/contest/2059/problem/C

# Contest: Codeforces Round 1002 (Div. 2)
# Date: February 2, 2025
# Author: Nishant Kumar
 
def solve():
    n = int(input())
    arr = []
    
    for _ in range(n):
        row = list(map(int, input().split()))
        arr.append(row)
    
    arr1 = [0] * n
    for i in range(n):
        for j in range(n - 1, -1, -1):
            if arr[i][j] != 1:
                break
            else:
                arr1[i] += 1
    
    arr1.sort()
    ans = 0
    for i in range(n):
        if arr1[i] >= ans:
            ans += 1
    
    print(ans)
 
if __name__ == "__main__":
    for _ in range(int(input())):
        solve()
 
# Author: Nishant Kumar
