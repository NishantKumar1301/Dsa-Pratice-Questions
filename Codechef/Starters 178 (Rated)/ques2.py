#Question : Placing 01 And 10
#Link to the question: https://www.codechef.com/START178B/problems/PLACE0110

# cook your dish here
for _ in range(int(input())):
    x,y = map(int,input().split())
    diff = abs(x-y)
    charge = diff-1 if diff>0 else 0
    print(x+y+charge)

