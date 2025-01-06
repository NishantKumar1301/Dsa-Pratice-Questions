#Question : Brightness Begins
#Link to the question: https://codeforces.com/contest/2020/problem/B


import math
 
def solve():
    test_cases = int(input())
    for _ in range(test_cases):
        target_value = int(input())
        left, right, answer = 1, 2 * 10**18, 0
 
        while left <= right:
            mid_value = (left + right) // 2
            sqrt_mid = math.isqrt(mid_value)  # Use isqrt for integer square root
 
            if mid_value - sqrt_mid >= target_value:
                answer = mid_value
                right = mid_value - 1
            else:
                left = mid_value + 1
 
        print(answer)
 
if __name__ == "__main__":
    solve()
