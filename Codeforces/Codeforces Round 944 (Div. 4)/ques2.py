#Question : Different String
#Link to the question: https://codeforces.com/contest/1971/problem/B

for _ in range(int(input())):
    s = list(input())  
    
    if len(set(s)) == 1:  
        print("NO")
    else:
        print("YES")
        for i in range(len(s) - 1):  
            if s[i] != s[i + 1]:  
                s[i], s[i + 1] = s[i + 1], s[i]  
                break
        print("".join(s)) 

