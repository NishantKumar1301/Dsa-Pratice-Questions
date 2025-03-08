#Question : Make It Zero
#Link to the question: https://codeforces.com/problemset/problem/1869/A

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    
    if n % 2 == 0: 
        print(2)
        print(1, n)
        print(1, n)
    else:  
        print(4)
        print(1, n - 1)
        print(1, n - 1)
        print(n - 1, n)
        print(n - 1, n)
