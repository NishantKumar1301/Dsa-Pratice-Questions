#Question : Halloumi Boxes
#Link to the question: https://codeforces.com/problemset/problem/1903/A


for _ in range(int(input())):
    n,k = map(int,input().split())
    arr = list(map(int,input().split()))
    sorted_arr = sorted(arr)
    if arr == sorted_arr:
        print("YES")
    elif k>1:
        print("YES")
    else:
        print("NO")
