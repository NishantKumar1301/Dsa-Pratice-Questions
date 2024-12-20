#Question :  Kevin and Binary Strings
#Link to the question: https://codeforces.com/contest/2048/problem/C

for _ in range(int(input())):
    s = input()
    n = len(s)
    index=-1 #Index will keep track of the first occurrence of 0
    #Find the index of first occurrence of 0
    for i in range(n):
        if s[i]=='0':
            index = i
            break
        
    #Count the number of consecutive zeroes 
    count =0
    if index!=-1:
        for i in range(index,n):
            if s[i]=='0':
                count+=1 
            else:
                break 
    
    #Observation:  first substring will be the entire substring always
    #if no zero is found then the second should contain only one 1 
    #if zero is found then the second substring should start with max(0,index-count)+1 
    #And ends at the index of min(index,count)
    
    ans =(0,0,0,0)
    if index==-1:
        ans =(1,n,1,1)
        # print(f"1 {n} 1 1")
    else:
        ans =(1,n,max(index-count,0)+1,n-min(index,count))
        # print(f"1 {n} {max(0,index-count)+1} {n-min(index,count)} ")
    print(*ans)