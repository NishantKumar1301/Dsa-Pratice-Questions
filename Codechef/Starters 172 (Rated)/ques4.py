#Question : Transform String
#Link to the question: https://www.codechef.com/problems/P4_172

# cook your dish here 
for _ in range(int(input())):
    a = input().strip()
    b = input().strip()
    
    ans,j,x,ind= 0,len(b)-1,len(b),-1
    for i in range(len(a)-1,-1,-1):
        if a[i]==b[j]:
            j-= 1 
            x-= 1 
        else: 
            ans += x+1
        if j<0:
            ind =i 
            break 
    if j>=0:
        print(-1)
    else:
        print(ans+ind)
    
    

