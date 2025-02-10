#Question : Skibidus and Ohio
#Link to the question: https://codeforces.com/contest/2065/problem/B

# Contest: Codeforces Round 1003 (Div. 4)
# Date: February 9, 2025
# Author: Nishant Kumar

def solve():
    n = input()
    # Write your logic here
    flag = False
    for i in range(len(n)-1):
        if n[i]==n[i+1]:
            flag = True
    if flag:
        print(1)
    else:
        print(len(n))


if __name__ == "__main__":
    for _ in range(int(input())):
        solve()

# Author: Nishant Kumar


