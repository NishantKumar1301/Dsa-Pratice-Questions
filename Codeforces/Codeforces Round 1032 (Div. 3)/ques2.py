#Question :  Above the Clouds
#Link to the question: https://codeforces.com/contest/2121/problem/B

# Contest: Codeforces Round 1032 (Div. 3)
# Date: June 17, 2025
# Author: Nishant Kumar

def solve():
    n = int(input())
    s= input()
    set_ = set()
    set_.add(s[0])
    set_.add(s[n-1])
    for i in range(1,n-1):
        if s[i] in set_:
            print("YES")
            return 
        set_.add(s[i])
    print("NO")


if __name__ == "__main__":
    for _ in range(int(input())):
        solve()

# Author: Nishant Kumar
