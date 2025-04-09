#Question : Flip Prefix
#Link to the question: https://www.codechef.com/START181B/problems/FLIPPRE?tab=ide

# cook your dish here
for _ in range(int(input())):
    n = int(input())
    s= input().strip()
    p=q=r=0
    for char in s:
        if char=='0':
            p+=1
        else:
            q+=1
        if p==q:
            r+=1
    print(2**r)



