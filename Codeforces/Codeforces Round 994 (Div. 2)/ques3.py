#Question : MEX Cycle
#Link to the question: https://codeforces.com/contest/2049/problem/C

"""Author : Nishant Kumar"""
#Function to find the mex_value
def find_mex(arr):
    mex=0
    while mex in arr:
        mex+=1
    return mex

def solve():
    n,x,y = map(int,input().split())
    adj =[[] for _ in range(n)] #Adjacency list to store the friends of each index
    for i in range(n):
        prev = n-1 if i==0 else i-1
        next = 0 if i==n-1 else i+1
        adj[i].append(prev)
        adj[i].append(next)

    # Add special friendship between x and y
    x-=1
    y-=1 #For converting x and y to 0 based indexing
    
    adj[x].append(y)
    adj[y].append(x)
    
    #Initialise the answer array with -1
    ans = [-1]*n 
    ans[x]=0  # Assign value 0 to dragon x
    ans[y]=1 # Assign value 0 to dragon y 
    
    # Assign values to remaining dragons based on MEX logic
    for i in range(n):
        if ans[i]==-1:#Assign the mex value only to the unassigned dragon
            # Collect values of friends
            used_value = set(ans[j] for j in adj[i] if ans[j]!=-1)
            ans[i]=find_mex(used_value)
    
    print(" ".join(map(str,ans)))



for _ in range(int(input())):
    solve()

"""Author : Nishant Kumar"""