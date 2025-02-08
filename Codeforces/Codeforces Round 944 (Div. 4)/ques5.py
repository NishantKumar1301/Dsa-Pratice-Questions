#Question : Find the Car
#Link to the question: https://codeforces.com/contest/1971/problem/E


import bisect

def solve():
    t = int(input())
    for _ in range(t):
        n, k, q = map(int, input().split())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        
        for _ in range(q):
            d = int(input())
            it = bisect.bisect_left(a, d) - 1
            
            if it == -1:
                dist = a[0]
                time = b[0]
                print((d * time) // dist, end=" ")
            else:
                dist = a[it + 1] - a[it]
                time = b[it + 1] - b[it]
                print(((d - a[it]) * time) // dist + b[it], end=" ")
        print()

solve()
