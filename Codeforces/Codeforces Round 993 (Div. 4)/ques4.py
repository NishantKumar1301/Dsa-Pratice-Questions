#Question : Harder Problem
#Link to the question: https://codeforces.com/contest/2044/problem/D

from collections import Counter
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    freq = Counter(arr)
    
    ans = []
    for i in range(1, n + 1):
        if i not in freq:
            ans.append(i)
    
    s = set()
    j = 0
    for i in range(n):
        if arr[i] not in s:
            print(arr[i], end=" ")
            s.add(arr[i])
        else:
            print(ans[j], end=" ")
            j += 1
    print()

