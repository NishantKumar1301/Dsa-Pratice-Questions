#Question : Kevin and Combination Lock
#Link to the question: https://codeforces.com/contest/2048/problem/A

for _ in range(int(input())):
    number = int(input())
    if number %33==0:
        print("YES")
    else:
        print("NO")