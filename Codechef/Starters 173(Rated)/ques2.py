#Question : Cool Subsequences
#Link to the question: https://www.codechef.com/problems/COOLSUB

# cook your dish here
def solve():
    n = int(input())
    arr = list(map(int,input().split()))
    freq ={}
    for n in arr:
        freq[n]=freq.get(n,0)+1
        if freq[n]>1:
            print(1)
            print(n)
            return
    print(-1)
for _ in range(int(input())):
    solve()
    
    