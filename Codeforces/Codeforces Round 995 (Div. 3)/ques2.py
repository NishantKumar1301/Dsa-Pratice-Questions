#Question : Journey
#Link to the question: https://codeforces.com/contest/2051/problem/B


"""
    Codeforces Round 995 (Div. 3)
    Author : Nishant Kumar
    Date : 22-12-2024
"""
 
def journey_ques2():
    n, a, b, c = map(int, input().split())
 
    total_sum = a + b + c
    p = n // total_sum
 
    if p * total_sum == n:
        print(3 * p)
        return
 
    if p * total_sum + a >= n:
        print(3 * p + 1)
        return
 
    if p * total_sum + a + b >= n:
        print(3 * p + 2)
        return
 
    if p * total_sum + a + b + c >= n:
        print(3 * p + 3)
        return
 
for _ in range(int(input())):
    journey_ques2()
 
"""Author : Nishant Kumar"""