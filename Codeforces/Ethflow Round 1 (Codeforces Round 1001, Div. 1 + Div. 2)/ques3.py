#Question : Cirno and Operations
#Link to the question: https://codeforces.com/contest/2062/problem/C

# Contest: Ethflow Round 1 (Codeforces Round 1001, Div. 1 + Div. 2)
# Date: 26-Jan-2025
# Author: Nishant Kumar
 
def solve():
    for _ in range(int(input())):
        n = int(input())
        arr = list(map(int, input().split()))
        ans = sum(arr)
        while n > 1:
            temp = [arr[i + 1] - arr[i] for i in range(n - 1)]
            ans = max(ans, abs(sum(temp)))
            
            arr = temp
            n -= 1
        
        print(ans)
 
if __name__ == "__main__":
    solve()
 
 
# Author: Nishant Kumar

