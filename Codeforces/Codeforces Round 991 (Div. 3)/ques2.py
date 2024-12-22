#Question : Transfusion
#Link to the question: https://codeforces.com/contest/2050/problem/B


"""Author : Nishant Kumar"""

def solve():
    n = int(input())
    arr = list(map(int,input().split()))
    even_sum = odd_sum =0
    for i in range(n):
        if i%2==0:
            even_sum+=arr[i]
        else:
            odd_sum+=arr[i]
            
    
    no_of_even_index =(n+1)//2
    no_of_odd_index=n//2
    
    if (even_sum%no_of_even_index==0 and odd_sum%no_of_odd_index==0 and (even_sum//no_of_even_index==odd_sum//no_of_odd_index)):
        print("YES")
    else:
        print("NO")
    



for _ in range(int(input())):
    solve()

"""Author : Nishant Kumar"""