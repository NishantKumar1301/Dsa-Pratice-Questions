#Question : Don't Try to Count
#Link to the question: https://codeforces.com/problemset/problem/1881/A

def check_substring(s,x):
    if len(s)>len(x):
        return False
    for i in range(len(x)-len(s)+1):
        if x[i:i+len(s)]==s:
            return True
    return False

def solve():
    n,m = map(int, input().split())
    x = input().strip()
    s= input().strip()
    # Write your logic here
    x0=x
    x1 = x0+x0
    x2 = x1+x1
    x3 = x2+x2
    x4 = x3+x3
    x5 = x4+x4
    ans =-1
    if check_substring(s,x0):
        ans =0
    elif check_substring(s,x1):
        ans =1
    elif check_substring(s,x2):
        ans =2
    elif check_substring(s,x3):
        ans =3
    elif check_substring(s,x4):
        ans =4
    elif check_substring(s,x5):
        ans =5
    print(ans)



if __name__ == "__main__":
    for _ in range(int(input())):
        solve()
