#Question : A Perfectly Balanced String?
#Link to the question: https://codeforces.com/contest/1673/problem/B
from collections import Counter
def check(s):
    n = len(s)
    freq = Counter(s)
    unique = len(freq)
    if unique==1:
        print("YES")
        return 
    
    mp={}
    flag = False
    
    for i in range(n):
        if s[i]  in mp:
            previous_occurence = mp[s[i]]
            curr = i 
            diff = curr -previous_occurence
            if diff != unique:
                flag=True
                break
            
        mp[s[i]]=i
        
    if flag:
        print("NO")
    else:
        print("YES")

for _ in range(int(input())):
    s = input()
    check(s)