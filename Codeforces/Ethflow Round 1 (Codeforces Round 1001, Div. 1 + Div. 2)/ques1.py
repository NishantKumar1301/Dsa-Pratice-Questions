#Question : String
#Link to the question: https://codeforces.com/contest/2062/problem/A

# Contest: Ethflow Round 1 (Codeforces Round 1001, Div. 1 + Div. 2)
# Date: 26-Jan-2025
# Author: Nishant Kumar
 
def solve():
    s= input()
    ans =0
    for char in s:
        if char =='1':
            ans+=1
    print(ans)
 
 
if __name__ == "__main__":
    for _ in range(int(input())):
        solve()
 
# Author: Nishant Kumar

