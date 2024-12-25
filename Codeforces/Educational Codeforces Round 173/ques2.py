#Question : Digits
#Link to the question:  https://codeforces.com/contest/2043/problem/B

"""Author : Nishant Kumar"""
 
def digit():
    n, d = map(int, input().split())
    answer_arr = []
    answer_arr.append(1)
 
    if n >= 3 or (n == 2 and d % 3 == 0):
        answer_arr.append(3)
 
    if d == 5:
        answer_arr.append(5)
 
    if n >= 3 or (n == 2 and d == 7):
        answer_arr.append(7)
 
    if n > 6 or (n == 2 and d == 9) or (3 <= n <= 5 and d in {3, 6, 9}) or n == 6:
        answer_arr.append(9)
 
    for num in answer_arr:
        print(str(num) + " ", end="")  
    print()  
 
testcase = int(input())
for _ in range(testcase):
    digit()
 
"""Author : Nishant Kumar"""
