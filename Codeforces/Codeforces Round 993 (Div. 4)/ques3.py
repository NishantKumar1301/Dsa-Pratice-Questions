#Question :  Hard Problem
#Link to the question: https://codeforces.com/contest/2044/problem/C

for _ in range(int(input())):
    m, a, b, c = map(int, input().split())
    
    row1 = min(m, a)  
    row2 = min(m, b) 
    
    rem_row1 = m - row1
    rem_row2 = m - row2
    
    extra1 = min(c, rem_row1)
    extra2 = min(c - extra1, rem_row2)
    
    ans = row1 + row2 + extra1 + extra2
    print(ans)
