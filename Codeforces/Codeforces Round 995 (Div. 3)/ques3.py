#Question : Preparing for the Exam
#Link to the question: https://codeforces.com/contest/2051/problem/C

"""
    Codeforces Round 995 (Div. 3)
    Author : Nishant Kumar
    Date : 22-12-2024
"""
 
def journey_ques2():
    n, m,k = map(int, input().split())
    arr1 = list(map(int,input().split()))
    arr2 = list(map(int,input().split()))
 
    s = set(arr2)
    
    arr3 = [i for i in range(1,n+1) if i not in s]
    
    if len(arr3) == 0:
        print("1" * m)
        
    elif len(arr3) == 1:
        single = arr3[0]
        ans = []
        for question in arr1:
            if question == single:
                ans.append("1")
            else:
                ans.append("0")
        print("".join(ans))
    else:
        print("0" * m)
    
    
 
for _ in range(int(input())):
    journey_ques2()
 
"""Author : Nishant Kumar"""
