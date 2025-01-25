#Question :  Left and Right Houses
#Link to the question: https://codeforces.com/contest/1945/problem/C



# Contest: Codeforces Round 935 (Div. 3)
# Date: 22-Jan-2025
# Author: Nishant Kumar

def solve():
    n = int(input())
    s = input()

    pre = [0] * n
    pre[0] = 1 if s[0] == '1' else 0
    for i in range(1, n):
        pre[i] = pre[i - 1] + (1 if s[i] == '1' else 0)

    def get_sum(l, r):
        if l == 0:
            return pre[r]
        return pre[r] - pre[l - 1]

    ans = -1
    if get_sum(0, n - 1) >= (n + 1) // 2:
        ans = 0

    for i in range(n):
        l1 = get_sum(0, i)  
        l0 = (i + 1) - l1  
        r1 = get_sum(i + 1, n - 1) if i + 1 < n else 0 
        r0 = (n - i - 1) - r1 

        if l0 >= l1 and r1 >= r0:
            if ans == -1 or abs(n - 2 * ans) > abs(n - 2 * (i + 1)):
                ans = i + 1

    if ans == -1:
        ans = 0
    print(ans)


if __name__ == "__main__":
    for _ in range(int(input())):
        solve()

# Author: Nishant Kumar
