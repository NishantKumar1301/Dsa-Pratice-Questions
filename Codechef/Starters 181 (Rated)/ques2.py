#Question : Breaking Sticks
#Link to the question: https://www.codechef.com/START181B/problems/BRKSTICK

# cook your dish here
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    ans = sum(arr)-n
    print(ans)

