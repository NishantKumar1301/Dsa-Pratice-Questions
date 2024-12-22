#Question : Best Price
#Link to the question:  https://codeforces.com/contest/2051/problem/E

"""Author : Nishant Kumar"""

from bisect import bisect_left

def solve():
    n, k = map(int, input().split())
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))
    
    arr1.sort()
    arr2.sort()
    
    arr3 = sorted(set(arr1 + arr2))
    
    ans = 0
    
    for val in arr3:
        # Use binary search to find the count of elements less than `val`
        a = bisect_left(arr1, val)
        b = bisect_left(arr2, val)
        
        diff = a - b
        
        if diff <= k:
            buyers = n - b  # Buyers from arr2 that can afford `val`
            earn = val * buyers
            ans = max(ans, earn)
    
    print(ans)

for _ in range(int(input())):
    solve()

"""Author : Nishant Kumar"""
