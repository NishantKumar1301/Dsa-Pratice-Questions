#Question : Uninteresting Number
#Link to the question: https://codeforces.com/contest/2050/problem/C

"""Author : Nishant Kumar"""

def solve():
    s = input().strip()
    number_of_2 = number_of_3 = total_sum=0
    for char in s:
        if char =='2':
            number_of_2+=1
        elif char =='3':
            number_of_3+=1
        total_sum+=int(char)
        
    ans =False
    for i in range(number_of_2+1): 
        for j in range(number_of_3+1):
            if (total_sum+2*i+2*j)%9==0:
                ans =True
                break
        if ans:
            break
    
    if ans:
        print("YES")
    else:
        print("NO")


for _ in range(int(input())):
    solve()

"""Author : Nishant Kumar"""
