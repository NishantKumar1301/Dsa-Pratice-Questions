#Question : Slavic's Exam
#Link to the question: https://codeforces.com/contest/1999/problem/D

for _ in range(int(input())):
    s = list(input().strip())  
    t = input().strip()
    
    i, n, m = 0, len(s), len(t)
    
    for j in range(m):
        while i < n and s[i] != t[j]:
            if s[i] == '?':
                s[i] = t[j] 
                break
            i += 1
        
        if i < n and s[i] == t[j]:
            i += 1
        else:
            print("NO")
            break
    else:
        print("YES")
        while i < n:
            if s[i] == '?':
                s[i] = 'n'  
            i += 1
        print("".join(s))  
