#Question : Sum and Product
#Link to the question: https://codeforces.com/contest/1857/problem/F

import math
from collections import Counter

def solve():
    n = int(input())
    arr = list(map(int,input().split()))
    query = int(input())
    freq = Counter(arr)
    for _ in range(query):
        x,y = map(int,input().split())
        if x*x <4*y:
            print(0,end=" ")
            continue
        val = x*x-4*y
        dis = int(math.isqrt(val))
        if dis*dis !=val:
            print(0,end=" ")
            continue
        roots = set()
        if (x+dis)%2==0:
            roots.add((x+dis)//2)
        if (x-dis)%2==0:
            roots.add((x-dis)//2)
        ans =0
        for ai in roots:
            aj = x-ai
            ans +=freq[ai]*freq[aj]
            if ai==aj:
                ans-=freq[ai]
        print(ans//2,end=" ")
    print()




for _ in range(int(input())):
    solve()

