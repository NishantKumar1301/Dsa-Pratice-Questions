#Question : Cost of the array
#Link to the question: https://codeforces.com/contest/2059/problem/B

# Contest: Codeforces Round 1002 (Div. 2)
# Date: February 2, 2025
# Author: Nishant Kumar
 
def solve_question2():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    
    if n == k:
        ind = -1
        for i in range(1, n, 2): 
            if a[i] != (i // 2) + 1:
                ind = (i // 2) + 1
                break
        if ind == -1:
            ind = (n // 2) + 1
        print(ind)
    else:
        ind = -1
        for i in range(1, n - k + 2):  
            if a[i] != 1:
                ind = i
                break
        
        if ind == -1:
            ans = 2
            for i in range(n - k, n, 2):  
                if a[i] != ans:
                    break
                ans += 1
            print(ans)
        else:
            print(1)
 
if __name__ == "__main__":
    n = int(input())
    for _ in range(n):
        solve_question2()
 
# Author: Nishant Kumar