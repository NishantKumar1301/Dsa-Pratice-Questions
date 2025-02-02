#Question : Milya and Two Arrays
#Link to the question: https://codeforces.com/contest/2059/problem/A

# Contest: Codeforces Round 1002 (Div. 2)
# Date: February 2, 2025
# Author: Nishant Kumar
 
def solve():
    n = int(input())
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))
    l1,l2 = len(set(arr1)),len(set(arr2))
    if l1+l2>3:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    for _ in range(int(input())):
        solve()
 
# Author: Nishant Kumar

