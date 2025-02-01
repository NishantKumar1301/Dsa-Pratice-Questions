#Question : Removals Game
#Link to the question: https://codeforces.com/contest/2002/problem/B   

for _ in range(int(input())):
    n = int(input())
    arr1 = list(map(int,input().split()))
    arr2 = list(map(int,input().split()))
    reversed_arr2 = arr2[::-1]
    if arr1 == arr2 or arr1 == reversed_arr2:
        print("Bob")
    else:
        print("Alice")

