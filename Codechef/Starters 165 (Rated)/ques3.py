#Question : Poster Perimeter
#Link to the question: https://www.codechef.com/problems/POSTPERI?tab=statement

# cook your dish here
for _ in range(int(input())):
    n,m,k= map(int,input().split())
    min_diff=float('inf')
    for l in range(1,n+1):
        for w in range(1,m+1):
            perimeter = 2*(l+w)
            min_diff = min(min_diff,abs(perimeter-k))   
    print(min_diff)
            
    



