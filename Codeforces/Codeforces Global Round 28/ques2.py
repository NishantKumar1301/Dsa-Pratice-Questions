#Question : Kevin and Permutation
#Link to the question: https://codeforces.com/contest/2048/problem/B

for _ in range(int(input())):
    n, k = map(int, input().split())
    arr = [0] * n 
    val = 1  
 
    for i in range(k - 1, n, k):
        arr[i] = val
        val += 1
 
    rem = n
    for i in range(n):
        if arr[i] == 0:
            arr[i] = rem
            rem -= 1
 
    print(" ".join(map(str, arr)))