#Question : Food Balance
#Link to the question: https://www.codechef.com/START178B/problems/FOODBAL

# cook your dish here
p,q,r,s = map(int,input().split())
x,y = abs(p-q),abs(r-s)
if x<y:
    print("First")
elif x==y:
    print("Both")
else:
    print("Second")

