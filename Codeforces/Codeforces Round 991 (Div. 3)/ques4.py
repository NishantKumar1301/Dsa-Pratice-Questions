#Question : Digital string maximization
#Link to the question: https://codeforces.com/contest/2050/problem/D

"""Author : Nishant Kumar"""

def solve():
    s= input().strip()
    digit = [int(ch) for ch in s]
    n = len(digit)
    for i in range(n):
        copy_i = i 
        while copy_i >0 and digit[copy_i]>0 and digit[copy_i]-1>digit[copy_i-1]:
            val = digit[copy_i]
            digit[copy_i]=digit[copy_i-1]
            digit[copy_i-1]=val-1
            if copy_i>0:
                copy_i-=1
            else:
                break
    print("".join(map(str,digit)))



for _ in range(int(input())):
    solve()

"""Author : Nishant Kumar"""