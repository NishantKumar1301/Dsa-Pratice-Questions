#Question : Counting Pairs
#Link to the question: https://codeforces.com/contest/2051/problem/D

"""
    Codeforces Round 995 (Div. 3)
    Author : Nishant Kumar
    Date : 22-12-2024
"""
 
import bisect as bs
 
def counting_pair():
    n, x, y = map(int, input().split())
    arr = list(map(int, input().split()))
    
    total = sum(arr)
    l = total - y
    r=total - x
    
    arr.sort()
    ans = 0
 
    for i in range(n - 1):
        low = l - arr[i]
        high = r - arr[i]
        
        left_check = bs.bisect_left(arr, low, i + 1, n)
        right_check = bs.bisect_right(arr, high, i + 1, n)
        ans += (right_check - left_check)
    
    print(ans)
 
test_case =int(input())
for _ in range(test_case):
    counting_pair()
 
"""Author : Nishant Kumar"""