#Question : Maximum Ones
#Link to the question: https://www.codechef.com/START180B/problems/MXON

# cook your dish here
for _ in range(int(input())):
    n,k = map(int,input().split())
    s=input()
    s= list(s)
    one = s.count('1')
    maxi =  one 
    for i in range(n-2,-1,-1):
        if s[i] == '0' and s[i + 1] == '1' and k > 0:
            s[i] = '1'
            k-=1 
            one+=1 
            maxi = max(maxi,one)
    print(maxi)
    
    
