#Question : Buttons
#Link to the question: https://codeforces.com/problemset/problem/1858/A

for _ in range(int(input()) ):
    a, b, c = map(int, input().split())
    
    if a == b:
        if c % 2 == 0:
            print("Second")
        else:
            print("First")
    elif a > b:
        print("First")
    else:
        print("Second")

