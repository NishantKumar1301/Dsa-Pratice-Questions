#Question : Skibidus and Rizz
#Link to the question: https://codeforces.com/contest/2065/problem/E

# Contest: Codeforces Round 1003 (Div. 4)
# Date: February 9, 2025
# Author: Nishant Kumar

def solve():
    n, m, k = map(int, input().split())
    char = ['0', '1']
    
    if n > m:
        n, m = m, n
        char[0], char[1] = char[1], char[0]

    if k < m - n or k > m:
        print("-1")
        return 

    ans = []
    while m > 0 or n > 0:  
        for _ in range(k):
            if m > 0:
                ans.append(char[1])
                m -= 1
        for _ in range(k):
            if n > 0:
                ans.append(char[0])
                n -= 1

    print("".join(ans))

if __name__ == "__main__":
    for _ in range(int(input())):
        solve()


# Author: Nishant Kumar


