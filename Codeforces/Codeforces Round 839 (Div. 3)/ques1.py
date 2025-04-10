#Question :  A+B?
#Link to the question: https://codeforces.com/contest/1772/problem/A

# cook your dish here
for _ in range(int(input())):
    arr = input().split('+')
    ans=0
    for char in arr:
        ans+=int(char)
    print(ans)

