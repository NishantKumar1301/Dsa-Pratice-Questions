#Question : Palindromic Score
#Link to the question: https://www.codechef.com/START182B/problems/LPSS

# cook your dish here
def helper(x,y):
    if x%2==0 or y%2==0:
        return x+y 
    return x+y-1

def solve(x,y,z):
    a = helper(y,z)
    b = helper(x,z)
    c = helper(x,y)
    return min(a,b,c)

for _ in range(int(input())):
    x,y,z = map(int,input().split())
    ans = solve(x,y,z)
    print(ans)