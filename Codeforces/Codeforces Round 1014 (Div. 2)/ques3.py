#Question : Asuna and the Mosquitoes
#Link to the question: https://codeforces.com/contest/2092/problem/C

# Contest: Codeforces Round 1014 (Div. 2)
# Date: March 29, 2025
# Author: Nishant Kumar

def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    sum_ = sum(arr)
    odd = 0
    for num in arr:
        if num%2==1:
            odd+=1
    if odd== 0 or odd==n:
        print(max(arr))
    else:
        ans = sum_-odd+1
        print(ans)    

if __name__ == "__main__":
    for _ in range(int(input())):
        solve()

# Author: Nishant Kumar